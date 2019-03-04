import twint
import csv
import ast
import pandas as pd

c = twint.Config()
c.Username = "bpjskesehatanri"
c.Since="2018-12-01"
c.Store_csv = True
c.Output = "hasildes"
twint.run.Search(c)
seen="notyetdetected"

with open('hasildes/tweets.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',')
     next(reader, None)
     for row in reader:
          try:
	          inreply=ast.literal_eval(row[12])
	          if seen == inreply[1]["screen_name"]: continue
	          
	          c = twint.Config()
	          seen = inreply[1]["screen_name"]
	          c.Username = seen	
	          c.Until=row[3]
	          c.Since="2018-12-01"
	          c.Store_csv = True
	          c.Output = "userdes"
	          try:	
	              twint.run.Search(c)
	          except TypeError:
	              print("Private User")
          except IndexError:
              print("doesnt have reply")


file_name = "userdes/tweets.csv"
file_name_output = "userdes/cleantweets.csv"
df = pd.read_csv(file_name, sep=",", engine='python')
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output)
#drop column1 after remove duplicates
#file_name = "userdes/cleantweets.csv"
#df = pd.read_csv(file_name, sep=",", engine='python')
#df.drop(df.columns[1], axis = 1, inplace = True) 
#df.to_csv("ngokcrot.csv")

#filter df2 only conversation in df1
df1 = pd.read_csv("hasildes/tweets.csv", sep=",", engine='python')
df2 = pd.read_csv("userdes/cleantweets.csv", sep=",", engine='python')
df2.drop(df2.columns[0], axis = 1,inplace = True) 
isonconv=df2.conversation_id.isin(df1.conversation_id)
repliedtweets=df2[isonconv]
repliedtweets.to_csv("userdes/repliedtweets.csv")


#read mention bpjskesehatanri on december
mentiondf = pd.read_csv("mentionbpjsdes/tweets.csv", sep=",", engine='python')
isrepliedby=mentiondf.conversation_id.isin(df1.conversation_id)
inaccountconversation=mentiondf[isrepliedby]
notbpjsaccount= inaccountconversation.username != 'bpjskesehatanri'
useraccount=inaccountconversation[notbpjsaccount]
useraccount.to_csv("userdes/inaccountconversationrepliedtweets.csv")

#follow up post complain
follow_up= df1.is_reply_to == 1
followuppost=df1[follow_up]

#kualitas dokter
kualitasdokter=useraccount.tweet.str.contains('dokter|Dokter')
dokter=useraccount[kualitasdokter]

positifdokter=dokter.tweet.str.contains('bagus|hebat|keren|puas|memuaskan|ramah|mudah|cepat')
pdok=dokter[positifdokter]

negatifdokter=dokter.tweet.str.contains('tidak empati|buru-buru|buru buru|tidak becus|malpraktek|malpraktik|tidak jelas|telat|kecewa|jelek|kacau|bobrok|mengecewakan|sulit|lama|ribet')
ndok=dokter[negatifdokter]

#kualitas obat
kualitasobat=useraccount.tweet.str.contains('obat|Obat|apotek|apotik')
obat=useraccount[kualitasobat]

positifobat=obat.tweet.str.contains('bagus|hebat|murah|keren|puas|memuaskan|ramah|mudah|cepat')
pobat=obat[positifobat]

negatifobat=obat.tweet.str.contains('buruk|mahal|habis|tidak tepat')
nobat=obat[negatifobat]

#kualitas staf
kualitasstaf=useraccount.tweet.str.contains('staf|perawat|pegawai|petugas')
staf=useraccount[kualitasstaf]

positifstaf=staf.tweet.str.contains('bagus|hebat|keren|puas|memuaskan|ramah|mudah|cepat')
pstaf=staf[positifstaf]

negatifstaf=staf.tweet.str.contains('kecewa|jelek|kacau|bobrok|mengecewakan|sulit|lama|ribet|tidak empati|tidak jelas')
nstaf=staf[negatifstaf]

#biaya/harga
kualitasharga=useraccount.tweet.str.contains('harga|biaya|iuran|bayar|bulan')
harga=useraccount[kualitasharga]

positifharga=harga.tweet.str.contains('bagus|hebat|keren|puas|memuaskan|ramah|mudah|cepat|murah|terjangkau')
pharga=harga[positifharga]

negatifharga=harga.tweet.str.contains('kecewa|jelek|kacau|bobrok|mengecewakan|sulit|lama|ribet|mahal')
nharga=harga[negatifharga]

#waktu tunggu
kualitaswaktu=useraccount.tweet.str.contains('waktu|tunggu|lama|menunggu')
waktu=useraccount[kualitaswaktu]

positifwaktu=waktu.tweet.str.contains('bagus|hebat|keren|puas|memuaskan|ramah|mudah|cepat|murah|terjangkau')
pwaktu=waktu[positifwaktu]

negatifwaktu=waktu.tweet.str.contains('kecewa|jelek|kacau|bobrok|mengecewakan|sulit|lama|ribet|mahal')
nwaktu=waktu[negatifwaktu]

