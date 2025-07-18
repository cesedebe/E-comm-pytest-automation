from demostore_automation.src.utilities.dbUtility import DBUtility
import random
import logging as logger

class ProductsDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_from_db(self, qty=1):
        """
        Gets a random product from db.
        :param qty: number of products to get
        :return:
        """

        logger.info(f"Getting random products from db. qty= {qty}")
        sql = f"""SELECT ID, post_title, post_name FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
        WHERE post_type = 'product' LIMIT 500;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_by_id(self, product_id):
        """
           Gets a product by ID from database.
           Parameters:
           product_id (str): ID of product to get
           Returns:
           list: database response.
        """

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE ID = {product_id};'''

        return self.db_helper.execute_select(sql)