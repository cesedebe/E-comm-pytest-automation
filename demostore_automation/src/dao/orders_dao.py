from demostore_automation.src.utilities.dbUtility import DBUtility
import random
import logging as logger

class OrdersDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_order_from_db(self, qty=1):
        """
        Gets a random order from db.
        :param qty: number of orders to get
        :return:
        """
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}wc_order_stats
                     ORDER BY order_id DESC LIMIT 5000;'''
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_order_lines_by_order_id(self, order_id):
        """
        Gets an order from order_id
        :param : None
        :return:
        """
        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}woocommerce_order_items 
                  WHERE order_id = {order_id};'''
        return self.db_helper.execute_select(sql)



