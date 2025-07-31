"""Assignment 2: Inventory checker with Tuples & Dicts"""
def parse_item(str_line: str) -> tuple[tuple | None, int | None]:
    """
    Parse 'category, name, quantity' into (key, value). 
    Key is a tuple (category, name). 
    """
    parts = [part.strip() for part in str_line.split(',')]
    if len(parts) == 3:
        try:
            key = (parts[0], parts[1])
            quantity = int(parts[2])
            return key, quantity
        except ValueError:
            return None, None
    return None, None

def populate_inventory(num_items: int) -> dict:
    """
    User input inventories
    """
    stock = {}
    print("--- Input inventory ---")
    
    for i in range(num_items):
        while True:
            input_str = input(f"Input #{i+1} (category, name, quantity): ")
            item_key, item_quantity = parse_item(input_str)
            if item_key is not None:
                stock[item_key] = item_quantity
                break
            else:
                print("Invalid query format")
    return stock

def query_inventory(stock: dict):
    """
    Query inventory
    """
    query_str = input("Enter inventory (category, name): ")
    
    try:
        query_parts = [part.strip() for part in query_str.split(',')]
        if len(query_parts) == 2:
            query_key = (query_parts[0], query_parts[1])
            quantity_found = stock.get(query_key, "Not found")
            print(f"Inventories left: {quantity_found}")
        else:
            print("Invalid query format")
    except Exception:
        print("Invalid query format")

def main():
    """
    Control inventories warehouse
    """
    inventory_numbers = int(input("Enter number of inventories: "))
    stock_data = populate_inventory(inventory_numbers)
    
    print("\n--- Warehouse dât ---")
    print(stock_data)
    
    query_inventory(stock_data)


if __name__ == "__main__":
    main()