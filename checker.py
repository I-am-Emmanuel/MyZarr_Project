import zarr
root = zarr.group()
root.attrs['1'] = "bar"
z1 = root.zeros('zoo', shape=(10000, 10000))
z1.attrs['bar'] = 72
z1.attrs['hol'] = 91
print(sorted(z1.attrs))
print(root.attrs['1'])


z1 = root.open('data/example.zarr', mode='w', shape=(10, 10), dtype='i4')