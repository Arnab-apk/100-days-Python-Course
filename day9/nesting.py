capitals={
    "France":"Pasis",
    "Germany":"Berlin"
}

# travel_log={
#     "France":["Pasis","Lille","Dijon"],
#     "Germany":["Berlin","Stugort"]
# }
#printing a specific element in a nestes dictionary
# print(travel_log["France"][1])
#nested lists
nested_list=["A","B",["C","D"]]
print(nested_list[2][1])

travel_log={
    "France":{
        "num_times visited":8,
        "cities_visited":["Pasis","Lille","Dijon"]
    },
    "Germany":{
    "cities_visited":["Stuttgart","Hamberg","Berlin"],
    "total-visits":5
    }
}
#printing complex nesting

print(travel_log["Germany"]["cities_visited"][0])




