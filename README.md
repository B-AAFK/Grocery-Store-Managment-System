# 🛒 Grocery Store Management System

This project is a lightweight web-based Grocery Store Management System built with Python (Flask) and MySQL. It allows users to manage products, orders, and units of measure through a RESTful API and provides basic UI integration options.

---

## ⚙️ Features

- 🧾 Manage products with pricing and units
- 📦 Insert and view orders with line-item details
- 🧮 Track total cost per order
- 🔄 CRUD operations via API endpoints
- 🌐 CORS-enabled for frontend interaction

---

## 🛠️ Technologies Used

- Python 3
- Flask (with RESTful routes)
- MySQL
- HTML/CSS (for frontend rendering)
- JavaScript (if extended)
- Custom DAO modules for clean database abstraction

---

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/B-AAFK/Grocery-Store-Managment-System.git
   cd grocery-store-system

2. Setup the Virutal environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Set up the database:
   - Ensure MySQL is running
   - Create a database grocery_store
   - Execute the sql schema script
  
CREATE TABLE `order` (
   `order_id` int NOT NULL AUTO_INCREMENT,
   `customer_name` varchar(100) NOT NULL,
   `total` double NOT NULL,
   `dateTime` datetime NOT NULL,
   PRIMARY KEY (`order_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

 CREATE TABLE `order_detail` (
   `order_id` int NOT NULL,
   `product_id` int NOT NULL,
   `quantity` double NOT NULL,
   `total_price` double NOT NULL,
   PRIMARY KEY (`order_id`),
   KEY `fk_product_id_idx` (`product_id`),
   CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) REFERENCES `order` (`order_id`) ON UPDATE RESTRICT,
   CONSTRAINT `fk_product_id` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON UPDATE RESTRICT
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

 CREATE TABLE `product` (
   `product_id` int NOT NULL AUTO_INCREMENT,
   `name` varchar(45) NOT NULL,
   `uom_id` int NOT NULL,
   `price_per_unit` double NOT NULL,
   PRIMARY KEY (`product_id`),
   KEY `uom_id_idx` (`uom_id`),
   CONSTRAINT `fk_uom_id` FOREIGN KEY (`uom_id`) REFERENCES `uom` (`uom_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

 CREATE TABLE `uom` (
   `uom_id` int NOT NULL AUTO_INCREMENT,
   `uom_name` varchar(45) NOT NULL,
   PRIMARY KEY (`uom_id`)
 ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

4. API Endpoints
   
  | Endpoint         | Method | Description            |
  | ---------------- | ------ | ---------------------- |
  | `/getUOM`        | GET    | Retrieve all UOMs      |
  | `/getProducts`   | GET    | Retrieve all products  |
  | `/insertProduct` | POST   | Insert a new product   |
  | `/deleteProduct` | POST   | Delete a product by ID |
  | `/getAllOrders`  | GET    | Retrieve all orders    |
  | `/insertOrder`   | POST   | Insert a new order     |

