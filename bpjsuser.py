import twint

c = twint.Config()

#c.Username = "bpjskesehatanri"
#c.Custom["tweet"] = ["id"]
#c.Custom["user"] = ["bio"]
#c.Limit = 10
c.Since="2018-12-22"
c.Until="2019-01-22"
c.Search = "@bpjskesehatanri"
c.Store_csv = True
c.Output = "bpjs"

twint.run.Search(c)