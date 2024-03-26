http_status  = 404

# else if
# if http_status == 200 or http_status == 201:
#     print("Success")
# elif http_status == 400:
#     print("Bad Request")
# elif http_status == 404:
#     print("Not Found")
# elif http_status == 500 or http_status == 501 :
#     print("Server error")
# else :
#     print("Unknown")

#switches -- did same thing that i did with else if using switches (match ---- it works same as switch statement)

match http_status :
    case 200 | 201:
        print("Succes")
    case 404:
        print("Not found")
    case _:
        print("Unknown") 