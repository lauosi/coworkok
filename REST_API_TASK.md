# Rest Api

Wykorzystując Django Rest Framework obsłużyć zapytanie GET, które przyjmuje opcjonalne parametry: city, count oraz date_start*, date_end*.
W odpowiedzi na zapytanie zwraca obiekt JSON zawierający listę biurek spełniających kryteria.

Obiekt JSON powinien mieć format:

{
  "desks":[
     {
        "city":"Wrocław",
        "company":"asd",
        "desk_price":22.0
     },
     {
        "city":"Wrocław",
        "company":"asd",
        "desk_price":22.0
     },
     {
        "city":"Wrocław",
        "company":"asd",
        "desk_price":22.0
     }
  ]
}

#### CBV, FBV, ViewSets + Routers
#### Serializacja
#### Permissions
