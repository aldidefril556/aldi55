
Meizu. py

 master
@aldidefril556
aldidefril556 committed 15 minutes ago 
0 parents commit 921cda29eb597b803a976e35e193470ec609ff84
Showing  with 68 additions and 0 deletions.
  68  meizu.py 
@@ -0,0 +1,68 @@
import os, sys

 print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

 print ("\033[1;32matau silahkan Hubungi MRR ")

 username = 'aldi123'      

 password = 'aldi321'



 def restart():

 	ngulang = sys.executable

 	os.execl(ngulang, ngulang, *sys.argv)



 def main():

 	uname = raw_input("username : ")

 	if uname == username:

 		pwd = raw_input("password : ")



 		if pwd == password:

 			print "\033[1;32mAlhmdllh sudah masuk juga..", 

 			sys.exit()



 		else:

 			print "\033[1;32mMaaf Masukkan password Anda salah... [?]\033[00m"

 			print "Silahkan segera log-in kembali...!!\n"

 			restart()



 	else:

 		print "\033[1;32mMaaf Masukkan Username Anda salah... [?]\033[00m"

 		print "Silahkan segera log-in kembali...!!\n"

 		restart()



 try:

 	main()

 except KeyboardInterrupt:

 	os.system('clear')

 	restart()

0 comments on commit 921cda2
@aldidefril556
 
 

Leave a comment

Attach files by selecting or pasting them.
 
 You’re receiving notifications because you’re watching this repository.
© 2019 GitHub, Inc.
