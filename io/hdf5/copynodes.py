import tables
import h5py

def get_dataset_keys(filename):
    """
    Return a list of all dataset keys in a HDF5 file
    Parameters
    ----------
    filename: str - path to the HDF5 file
    Returns
    -------
    list of keys
    """
    dataset_keys = []

    def walk(name, obj):
        if type(obj) == h5py._hl.dataset.Dataset:
            dataset_keys.append(name)

    with h5py.File(filename, "r") as file:
        file.visititems(walk)

    return dataset_keys



def copy_nodes(src, dest, keys=None):
    """
    copy all nodes listed in keys
    (if keys is None, copy everything)
    """
    if keys is None:
        keys = get_dataset_keys(src)
    with tables.open_file(src, 'r') as s:
        with tables.open_file(dest, 'a') as d:
            for k in keys:
                if not k.startswith('/'):
                    k = '/' + k

                path, name = k.rsplit('/', 1)
                if path not in d:
                    grouppath, groupname = path.rsplit('/', 1)
                    g = d.create_group(
                    grouppath, groupname, createparents=True
                    )
                else:
                    g = d.get_node(path)
                s.copy_node(k, g, overwrite=True)
