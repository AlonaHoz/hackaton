import tabulate
import UserDataMangment

head = ["Username", "Score"]

mydata = [
    [UserDataMangment.the_list[2], "100"],
    ["mia", "92"],
    ["alisa", "79"],
      ["elia", "66"]
]

table = tabulate.tabulate(mydata, headers=head)
print(table)