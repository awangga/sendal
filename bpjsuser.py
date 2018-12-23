import twint

c = twint.Config()

#c.Username = "bpjskesehatanri"
#c.Custom["tweet"] = ["id"]
#c.Custom["user"] = ["bio"]
#c.Limit = 10
c.Since="2018-12-01"
c.Search = "@bpjskesehatanri"
c.Store_csv = True
c.Output = "mentionbpjsdes"

twint.run.Search(c)