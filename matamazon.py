import json
import argparse
import sys

class InvalidIdException(Exception):
    "id is not valid according to the specification"

class InvalidPriceException(Exception):
    "price is not valid according to the specification"

class Customer:
    """
    Represents a customer in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Customer name.
        - city (str): Customer city.
        - address (str): Customer shipping address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Customer(id=42, name='Daniel Elgarici', city='Karmiel, address='123 Main Street')
        Exact formatting requirements appear in the assignment PDF.
    """

    # TODO implement this class as instructed

    def __init__(self, id, name, city, address):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id
        self.name = name
        self.city = city
        self.address = address
    
    def get_Name(self):
        return self.name
    def set_Name(self, newName):
        self.name = newName
    def get_ID(self):
        return self.id
    def set_ID(self, id):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id
    def set_City(self, city):
        self.city = city
    def get_City(self):
        return self.city
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def __str__(self):
        return f"Customer(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"   
    __repr__ = __str__

class Supplier:
    """
    Represents a supplier in the Matamazon system.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Supplier name.
        - city (str): Warehouse city (origin city for shipping).
        - address (str): Warehouse address.

    Exceptions:
        InvalidIdException: If 'id' is not valid according to the specification.

    Printing:
        Must support printing in the following format (example):
            Supplier(id=42, name='Yinon Goldshtein', city='Haifa, address='32 David Rose Street')
    """

    # TODO implement this class as instructed
    def __init__(self, id, name, city, address):
        if (id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id
        self.name = name
        self.city = city
        self.address = address
    
    def get_Name(self):
        return self.name
    def set_Name(self, newName):
        self.name = newName
    def get_ID(self):
        return self.id
    def set_ID(self, id):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id
    def set_City(self, city):
        self.city = city
    def get_City(self):
        return self.city
    def get_address(self):
        return self.address
    def set_address(self, address):
        self.address = address
    def __str__(self):
        return f"Supplier(id={self.id}, name='{self.name}', city='{self.city}', address='{self.address}')"
    __repr__ = __str__

class Product:
    """
    Represents a product sold on the Matamazon website.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier.
        - name (str): Product name.
        - price (float): Non-negative price.
        - supplier_id (int): ID of the supplier that provides the product.
        - quantity (int): Non-negative quantity in stock.

    Exceptions:
        InvalidIdException:
            - If id/supplier_id/quantity is invalid per specification.
        InvalidPriceException:
            - If price is invalid (e.g., negative).

    Printing:
        Must support printing in the following format (example):
            Product(id=101, name='Harry Potter Cushion', price=29.99, supplier_id=42, quantity=555)
    """

    def __init__(self, id, name, price, supplier_id, quantity):
        if id < 0 or supplier_id < 0 or quantity < 0:
            raise InvalidIdException("ID must be non-negative.")

        if price < 0:
            raise InvalidPriceException("Price must be non-negative.")

        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id
        self.quantity = quantity
    
    def get_Name(self):
        return self.name
    def set_Name(self, newName):
        self.name = newName
    def get_ID(self):
        return self.id
    def set_ID(self, id):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id
    def set_supplierID(self, supplier_ID):
        if supplier_ID < 0:
            raise InvalidIdException("ID must be non-negative.")
        
        self.supplier_id = supplier_ID
    def get_SupplierID(self):
        return self.supplier_id
    def get_quantity(self):
        return self.quantity
    def set_quantity(self, quantity):
        if(quantity>=0):
            self.quantity = quantity
        else:
            raise ValueError("quantity must be non-negative")
    def reduce_quantity(self,num):
        self.quantity-=num
        if (self.quantity < 0):
            self.quantity = 0
    def set_Price(self, price):
        if(price>=0):
            self.price = price
        else:
            raise InvalidPriceException("Price must be non-negative.")
    def get_Price(self):
        return self.price
    def __str__(self):
        return (
            f"Product(id={self.id}, "
            f"name='{self.name}', "
            f"price={self.price}, "
            f"supplier_id={self.supplier_id}, "
            f"quantity={self.quantity})"
        )    
    def __lt__(self, other):
        if self.price != other.price:
            return self.price < other.price
        return self.id < other.id
    __repr__ = __str__



class Order:
    """
    Represents a placed order.

    Required fields (per specification):
        - id (int): Unique non-negative integer identifier (assigned by the system).
        - customer_id (int): ID of the customer who placed the order.
        - product_id (int): ID of the ordered product.
        - quantity (int): Ordered quantity (non-negative integer).
        - total_price (float): Total price for the order (non-negative).

    Exceptions:
        InvalidIdException:
            - If one of the ID fields is invalid.
        InvalidPriceException:
            - If total_price is invalid.

    Printing:
        Must support printing in the following format (example):
            Order(id=1, customer_id=42, product_id=101, quantity=10, total_price=299.9)

    """

    # TODO implement this class as instructed
    def __init__(self, id, customer_id, product_id, quantity, total_price):
        if id < 0 or customer_id < 0 or product_id < 0 or quantity < 0:
            raise InvalidIdException("ID must be non-negative.")
        if total_price < 0:
            raise InvalidPriceException("Price must be non-negative.")
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        return (
            f"Order(id={self.id}, "
            f"customer_id={self.customer_id}, "
            f"product_id={self.product_id}, "
            f"quantity={self.quantity}, "
            f"total_price={self.total_price})"
        )    
    def setID(self, id):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.id = id;
    def getID(self):
        return self.id
    def getcustomer_id(self):
        return self.customer_id
    def setcustomer_id(self, id):
        if(id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.customer_id = id
    def setproduct_id(self, product_id):
        if(product_id < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.product_id = product_id
    def getproduct_id(self):
        return self.product_id
    def getQuantity(self):
        return self.quantity
    def setquantity(self, quantity):
        if(quantity < 0):
            raise InvalidIdException("ID must be non-negative.")
        self.quantity = quantity
    def gettotal_price(self):
        return self.total_price
    def settotal_price(self, price):
        if(price < 0):
            raise InvalidPriceException("Price must be non-negative.")
        self.total_price = price
    __repr__ = __str__

class MatamazonSystem:
    """
    Main system class that stores and manages customers, suppliers, products and orders.

    The system must support:
        - Registering customers/suppliers (with unique IDs across both types).
        - Adding/updating products (must validate supplier existence).
        - Placing orders (validate product existence and stock).
        - Removing objects by ID and type (with dependency constraints).
        - Searching products by name/query and optional max price.
        - Exporting system state to a text file (customers/suppliers/products only).
        - Exporting orders to JSON grouped by supplier origin city.

    Notes:
        - The specification does not require specific internal fields. Any data structures are allowed,
          as long as the behaviors match the spec.
        - A parameterless constructor is required.
    """

    def __init__(self): #done?
        self.suppliers = {}
        self.customers = {}
        self.orders = {}
        self.products = {}
        self.orderNum = 1
        """
        Initialize an empty Matamazon system.

        Requirements:
            - Must be parameterless.
            - Internal collections may be chosen freely (dict/list, etc.).
        """


    def register_entity(self, entity, is_customer): #done
        """
        Register a Customer or Supplier in the system.
        Args:
            entity: A Customer or Supplier object.
            is_customer (bool): True if entity is Customer, False if entity is Supplier.

        Raises:
            InvalidIdException:
                - If the entity ID is invalid.
                - If the entity ID already exists in the system (note: IDs must be unique across
                  customers AND suppliers).
        """
        if entity.id in self.customers and entity.id in self.suppliers:
            raise InvalidIdException("ID already exists.")

        if is_customer:
            self.customers[entity.id] = entity
        else:
            self.suppliers[entity.id] = entity



    def add_or_update_product(self, product): #done
        """
        Add a new product or update an existing product.

        Behavior:
            - If product does not exist in system: add it.
            - If product exists:
                - It must belong to the same supplier as the existing one (same supplier_id),
                  otherwise raise InvalidIdException.
                - Update the stored product's fields according to the new product.

        Args:
            product: A Product object.

        Raises:
            InvalidIdException:
                - If the supplier_id does not exist in the system.
                - If attempting to update a product but supplier_id differs from the existing product.
        """
        if product.supplier_id not in self.suppliers:
            raise InvalidIdException("Supplier does not exist.")

        if product.id not in self.products:
            self.products[product.id] = product
        else:
            old_prod = self.products[product.id]

            if old_prod.supplier_id != product.supplier_id:
                raise InvalidIdException("Supplier mismatch.")

            old_prod.name = product.name
            old_prod.price = product.price
            old_prod.quantity = product.quantity

    def place_order(self, customer_id, product_id, quantity=1): #done
        """
        Place an order for a product by a customer.

        Args:
            customer_id (int): Customer ID.
            product_id (int): Product ID.
            quantity (int, optional): Quantity to order. Defaults to 1.

        Returns:
            str: Status message according to specification:
                - "The order has been accepted in the system"
                - "The product does not exist in the system"
                - "The quantity requested for this product is greater than the quantity in stock"

        Behavior:
            - If product does not exist: return the relevant message.
            - If quantity requested > stock: return the relevant message.
            - Otherwise:
                - Decrease product stock by quantity.
                - Create a new Order with an auto-incremented system ID (starting at 1).
                - Store the order in the system.
                - Return success message.

        Notes:
            - The specification assumes quantity is an integer.
        """
        if customer_id not in self.customers:
            raise InvalidIdException("Customer does not exist.")

        if product_id not in self.products:
            return "The product does not exist in the system"
        num = self.orderNum
        price = self.products[product_id].get_Price()
        if quantity > self.products[product_id].get_quantity():
            return "The quantity requested for this product is greater than the quantity in stock"
        self.products[product_id].reduce_quantity(quantity)
        newOrder = Order(num, customer_id, product_id, quantity, round(price*quantity,2))
        self.orders[num] = newOrder
        self.orderNum+=1
        return "The order has been accepted in the system"

    def remove_object(self, _id, class_type):
        """
        Remove an object from the system by ID and type.

        Args:
            _id (int): Object ID to remove.
            class_type (str): One of: "Customer", "Supplier", "Product", "Order"
                              (exact casing/spelling per assignment).

        Returns:
            int | None:
                - If removing an Order: return the ordered quantity of that order (to restore stock).
                - Otherwise: no return value required.

        Raises:
            InvalidIdException:
                - If _id is not a valid non-negative integer.
                - If attempting to remove a Customer/Supplier/Product that still has dependent orders
                  in the system (i.e., orders that were not removed).
                - Additional InvalidIdException conditions as required by specification.
        """
        class_type = class_type.strip().capitalize()
        if(_id < 0):
            raise InvalidIdException("ID must be non-negative.")
        if(class_type == "Customer"):
            if _id not in self.customers:
                raise InvalidIdException("Customer does not exist.")
            for order in self.orders.values():
                if order.customer_id == _id:
                    raise InvalidIdException("Cannot remove a customer with an existing order.")

            self.customers.pop(_id)
        elif class_type == "Supplier":
            if _id not in self.suppliers:
                raise InvalidIdException("Supplier does not exist.")
            for order in self.orders.values():
                product = self.products.get(order.product_id)
                if product and product.supplier_id == _id:
                    raise InvalidIdException("ID cannot be removed")

            self.suppliers.pop(_id)
        elif (class_type == "Product"):
            if _id not in self.products:
                raise InvalidIdException("Product does not exist.")
            for order in self.orders.values():
                if order.product_id == _id:
                    raise InvalidIdException("ID cannot be removed.")
            self.products.pop(_id)
        elif class_type == "Order":
            if _id not in self.orders:
                raise InvalidIdException("Order does not exist.")
            order = self.orders.pop(_id)
            product = self.products.get(order.product_id)
            if product:
                product.quantity += order.quantity
            return order.quantity
        else:
            raise InvalidIdException("Unknown class type.")



    def search_products(self, query, max_price=None): #done-ish
        """
        Search products by query in the product name, and optionally filter by max_price.

        Args:
            query (str): Product name or part of product name.
            max_price (float, optional): If provided, only return products with price <= max_price.

        Returns:
            list[Product]:
                - Products that match the query and have quantity != 0,
                - Sorted by ascending price.
                - If no matching products exist, return an empty list.
        """
        query_str = str(query).replace("_", " ").lower()
        right_products = []
        if max_price is not None:
            max_price = float(max_price)
        for product in self.products.values():
                if product.quantity > 0:
                    if query_str in product.get_Name().lower():
                        if max_price is None or product.get_Price() <= max_price:
                            right_products.append(product)

        return sorted(right_products)


    def export_system_to_file(self, path):
        """
        Export system state (customers, suppliers, products) to a text file.

        Args:
            path (str): Output file path.

        Behavior:
            - Write each object on its own line, using the object's print/str representation.
            - Orders must NOT be included.
            - No constraint on the ordering of objects in the output.

        Raises:
            OSError (or any file-open exception): Must be propagated to the caller.
        """
        with open(path, "w", encoding="utf-8") as file:
            for customer in self.customers.values():
                file.write(str(customer) + '\n')
            for supplier in self.suppliers.values():
                file.write(str(supplier) + "\n")
            for product in self.products.values():
                file.write(str(product) + "\n")


    def export_orders(self, out_file):
        """
        Export orders in JSON format grouped by origin city.

        Args:
            out_file (file-like)

        Behavior (per specification):
            - Produce a JSON object where:
                - Keys: origin city (supplier city) for each order.
                - Values: list of strings representing orders (format as specified in section 4.1.4).
            - Order lists can be in any order.
            - No requirement on key ordering.

        Raises:
            Any exception during writing: Must be propagated to the caller.

        Notes:
            - The order origin city is the supplier city of the ordered product.
        """
        
        result = {}
        for order in self.orders.values():
            product = self.products.get(order.product_id)
            if product and product.supplier_id in self.suppliers:
                city = self.suppliers[product.supplier_id].city
                result.setdefault(city, []).append(str(order))
        json.dump(result, out_file)
    # If out_file is a path string, open it; if it's a file-like object, write/dump to it
       #"""  if isinstance(out_file, str):
        #    with open(out_file, "w", encoding="utf-8") as f:
         #       json.dump(result, f)
        #else: """
        
                        
        


def load_system_from_file(path):
    """
    Load a MatamazonSystem from an input file.

    Args:
        path (str): Path to a text file containing customers, suppliers and products.

    Returns:
        MatamazonSystem: Initialized system with the data found in the file.

    Behavior:
        - The file lines contain objects in the format produced by export_system_to_file (section 4.2).
        - Lines may appear in any order (e.g., product lines can appear before supplier lines).
        - Illegal lines may be ignored.
        - If an exception occurs during the creation of any required object due to invalid data,
          the function should stop and propagate the exception (as specified).

    Notes:
        - The assignment hints that eval() may be used.
    """
    system = MatamazonSystem()

    # The system file uses the same textual format produced by
    # export_system_to_file / print(obj) — e.g.
    #   Customer(id=1, name='Dana', city='Haifa', address='1 St')
    # Since the printed keyword names match the constructors' parameter
    # names exactly, eval() reconstructs the object directly.
    eval_globals = {"Customer": Customer, "Supplier": Supplier, "Product": Product}

    customers_and_suppliers = []
    products = []

    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            try:
                obj = eval(line, eval_globals)
            except (InvalidIdException, InvalidPriceException):
                # A real object was being built but the data was invalid:
                # per spec, stop and propagate this exception.
                raise
            except Exception:
                # Not a valid Customer/Supplier/Product line -> ignore it.
                continue

            if isinstance(obj, Product):
                products.append(obj)
            elif isinstance(obj, (Customer, Supplier)):
                customers_and_suppliers.append(obj)
            # anything else eval() might produce is silently ignored

    for entity in customers_and_suppliers:
        system.register_entity(entity, isinstance(entity, Customer))

    for product in products:
        system.add_or_update_product(product)

    return system
    

def execute_script(system, script_file_path):
    """
    Opens the script file and executes every command in it.
    """
    with open(script_file_path) as script_file:
        for command in script_file:
            execute_script_command(system, command)

def execute_script_command(system, command):
    """
    Executes a single command from the script file.
    """

    line_pieces = command.strip().split()

    if not line_pieces:
        return

    command = line_pieces[0]

    if command == "register":
        if line_pieces[1] == "customer":
            customer = Customer(
                int(line_pieces[2]),
                line_pieces[3].replace("_", " "),
                line_pieces[4].replace("_", " "),
                line_pieces[5].replace("_", " ")
            )
            system.register_entity(customer, True)

        else:
            supplier = Supplier(
                int(line_pieces[2]),
                line_pieces[3].replace("_", " "),
                line_pieces[4].replace("_", " "),
                line_pieces[5].replace("_", " ")
            )
            system.register_entity(supplier, False)

    elif command == "add":
        product = Product(
            int(line_pieces[1]),
            line_pieces[2].replace("_", " "),
            float(line_pieces[3]),
            int(line_pieces[4]),
            int(line_pieces[5])
        )

        system.add_or_update_product(product)

    elif command == "update":
        product = Product(
            int(line_pieces[1]),
            line_pieces[2].replace("_", " "),
            float(line_pieces[3]),
            int(line_pieces[4]),
            int(line_pieces[5])
        )

        system.add_or_update_product(product)

    elif command == "order":
        if len(line_pieces) == 3:
            system.place_order(
                int(line_pieces[1]),
                int(line_pieces[2])
            )
        else:
            system.place_order(
                int(line_pieces[1]),
                int(line_pieces[2]),
                int(line_pieces[3])
            )

    elif command == "remove":
        system.remove_object(
            int(line_pieces[2]),
            line_pieces[1].capitalize()
        )

    elif command == "search":
        if len(line_pieces) > 2:
            results = system.search_products(
                line_pieces[1].replace("_", " "),
                float(line_pieces[2])
            )
        else:
            results = system.search_products(line_pieces[1].replace("_", " "))

        print(results)

USAGE_MESSAGE = (
    "Usage: python3 matamazon.py -l < matamazon_log > -s < matamazon_system > "
    "-o <output_file> -os <out_matamazon_system>"
)


class MatamazonArgumentParser(argparse.ArgumentParser):
    """Argument parser that prints the exact required usage message and
    exits with code 1 on any bad/missing/unknown flag, instead of
    argparse's default error message/exit-code-2 behavior."""

    def error(self, message):
        print(USAGE_MESSAGE, file=sys.stderr)
        exit(1)


def main():
    # Create the argument parser
    parser = MatamazonArgumentParser(add_help=False, allow_abbrev=False)

    parser.add_argument("-l", dest="log_file")           # Log/script file (required)
    parser.add_argument("-s", dest="system_file")        # Existing system file (optional)
    parser.add_argument("-o", dest="output_file")        # Orders JSON export (optional)
    parser.add_argument("-os", dest="out_system_file")   # System export (optional)

    # Read the command-line arguments
    args = parser.parse_args()

    # A log/script file is required
    if args.log_file is None:
        parser.error("missing required -l flag")

    # Load an existing system if supplied,
    # otherwise create an empty one.
    system = (
        load_system_from_file(args.system_file)
        if args.system_file
        else MatamazonSystem()
    )

    # Execute all commands in the log file
    execute_script(system, args.log_file)

    # Export the current system (customers, suppliers, products)
    if args.out_system_file:
        system.export_system_to_file(args.out_system_file)

    # Export orders
    if args.output_file:
        with open(args.output_file, "w") as file:
            system.export_orders(file)
    else:
        # If no output file was given,
        # print the JSON to the terminal.
        system.export_orders(sys.stdout)
import traceback
if __name__ == "__main__":
    try:
        main()
    #except Exception:
     #   traceback.print_exc()
    except Exception:
       print("The matamazon script has encountered an error" + "\n")
       sys.exit(0)
    #except Exception as e:
     #   print(e)
      #  raise
