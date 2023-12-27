# Ganti nilai var_list dengan list yang sebenarnya
var_list = [4, 8, 15, 16, 23, 42, 605132, 7, 605132, 9, 11, 13]

# Panjang list
new_var = var_list
panjang = len(new_var)

# Nilai maksimal list
new_var1 = var_list
maksimal = max(new_var1)

# Nilai minimal list
new_var2 = var_list
minimal = min(new_var2)

# Banyaknya angka 605132 dalam list
banyak = var_list.count(605132)

# Menampilkan hasil
print("Panjang list:", panjang)
print("Nilai maksimal:", maksimal)
print("Nilai minimal:", minimal)
print("Banyaknya angka 605132:", banyak)
