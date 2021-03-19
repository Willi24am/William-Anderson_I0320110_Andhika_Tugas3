# list teman saya
list = ['Ricky', 'David', 'Budi', 'Bryant', 'Andre', 'Alex', 'Willy', 'Dzaki', 'Ben', 'Valerian']

print(list[4], list[6], list[7])

# mengganti list indeks nomor 3,5,9
list[3] = 'Ravi'
list[5] = 'Husnul'
list[9] = 'Dzidhan'

print(list)

# menambah teman pada list
list.extend(["Yeario", "Togar"])

print(list)

# menampilkan teman dengan perulangan
print ("Teman saya ada : {} orang".format (len(list)))
for teman in list:
    print (teman)

# menampilkan panjang list
print(len(list))