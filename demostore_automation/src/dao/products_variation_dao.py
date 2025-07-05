from demostore_automation.src.utilities.dbUtility import DBUtility
import random
import logging as logger

class ProductsVariationDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_product_with_variation(self , qty=1):
        """
        Gets a random product with variation from db.
        :param qty: number of products to get
        :return:
        """

        logger.info(f"Getting random product with variation from db. qty= {qty}")
        sql = f"""SELECT DISTINCT p.ID AS product_id, p.post_title AS product_name
                    FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts AS p
                    INNER JOIN {self.db_helper.database}.{self.db_helper.table_prefix}posts AS pv ON p.ID = pv.post_parent
                    WHERE p.post_type = 'product' AND pv.post_type = 'product_variation';"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))


    def get_random_product_variation_from_db(self, qty=1):
        """
        Gets a random product variation from db.
        :param qty: number of products to get
        :return:
        """

        logger.info(f"Getting random products variation from db. qty= {qty}")
        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
        WHERE post_type = 'product_variation' LIMIT 500;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_product_variation_by_id(self, product_id):
        """
           Gets a product variation by ID from database.
           Parameters:
           product_id (str): ID of product variation to get
           Returns:
           list: database response.
        """

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE post_type = 'product_variation' AND ID = {product_id};'''

        return self.db_helper.execute_select(sql)