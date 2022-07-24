# DRY - don't repeat yourself;
#
#
#
import csv
#
def get_new_html_product(img: str, sale: str, affiliat: str, title: str, price: str) -> str: 
    """
        This function return HTML template for my future pages. I respect DRY rule;
    """

    html_template = f"""
    <div class="w3-container">
        <div class="w3-display-container">
          <img src="{img}" style="width:65%">
          <span class="w3-tag w3-display-topleft">{sale}</span>
          <div class="w3-display-middle w3-display-hover">
          <a href = "{affiliat}" target="_blank"
            <button class="w3-button w3-black">Vezi produsul <i class="fa fa-shopping-cart"></i></button>
            </a>
          </div>
        </div>
        <a href = "{affiliat}" target="_blank"
        <p>{title}
        </a>
        <br>
        
        <b>{price}</b></p>
      </div>
            """

    return html_template


def return_list_from_csv(path: str) -> list:
    """
        This function open a CSV file. Respect DRY rule;
    """
    
    # list with html_data;
    list_with_html_data = []

    with open(path, 'r') as file:       
        csv_reader = csv.reader(file)

        for row in csv_reader:
            if "affiliat_link" in row:
                continue
                    
            else: 
                title = row[1]
                price = row[2]
                sale = row[3]
                img = row[4]
                affiliat = row[5]  
            
            html_template = get_new_html_product(img, sale, affiliat, title, price)
            list_with_html_data.append(html_template)
    
    return list_with_html_data