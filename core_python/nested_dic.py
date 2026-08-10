mystudent={
"stu1":
{"name":"mhk",
"class":"bca",
"age":21
},                           #nested dic ko {} se mention
                               # krke multiple values de dete he

"stu2":
{"name":"mahi",
"class":"bca",
"age":20
},

"stu3":
{"name":"akki",
"class":"bca",
"age":22
},


"stu4":
{"name":"spna",
"class":"bca",
"age":22
}
}
print(mystudent)
print(mystudent["stu1"]["age"])    #dic name or specific value ko access krne ke liye [] square bracket ke thorugh kisi bhi sspecific value le skte he

for k,v_obj in mystudent.items():   # here v_obj will hold the object (nested dictionary)
    print(k)
    for st_key in v_obj: #code will return each key value
        print (st_key +':',v_obj[st_key])