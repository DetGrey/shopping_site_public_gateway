# Public Gateway
Håndterer registrerede produkter og brugernes indkøbskurve.

## API Endpoints

### Cart Service
#### See all cart items

- **URL:** `/cart`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns cart data
  - **204 No contet:** Cart is empty
  - **500:** Some error happened

#### Add new item to cart

- **URL:** `/cart`
- **Method:** `POST`
- **Request Body:** JSON

  ```json
  {
      "product_id": 4321,
      "amount": 1
  }
  ```

- **Response:**

  - **201 Created:** Item added to cart successfully
  - **500:** Some error happened

#### Delete item from cart

- **URL:** `/cart/<id>`
- **Method:** `DELETE`

- **Response:**

  - **204 No content:** Item deleted from cart successfully
  - **404 Not Found:** Item not found
  - **500:** Some error happened

#### Update product amount

- **URL:** `/cart/<id>`
- **Method:** `PATCH`
- **Request Body:** JSON

  ```json
  {
      "amount": 2
  }
  ```

- **Response:**

  - **200 OK:** Product amount updated successfully
  - **400:** Specifying amount is required
  - **500:** Some error happened

### Product Catalog Service

#### View All products

- **URL:** `/products`
- **Method:** `GET`

- **Response:**

  - **200 OK:** Returns all product data

#### View Single Product

Product IDs in this database are 4 digits

- **URL:** `/products/<product_id>`
- **Method:** `GET`

- **Response**
    - **200 OK:** Return product data
    - **404 Not Found:** Product not found

#### Create new product

- **URL:** `/products`
- **Method:** `POST`

- **Request body:** JSON

```json
{
    "product_id": "<Product ID : Int>" ,
    "title": "<Title : Str>",
    "description": "<Product Description : Str>",
    "category": "<Category : Str>",
    "price": "<Price : Double>",
    "rating": "<Product Rating : Int>",
    "stock": "<Stock of product : Int>"
}

```

- **Response**
    - **201 Created:** 
    - **400 Bad Request:** Missing Data in Body
    - **409 Conflict:** Product already exists
    - **500 Error:** Connection error