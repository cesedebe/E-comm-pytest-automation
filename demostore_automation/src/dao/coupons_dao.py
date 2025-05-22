

from demostore_automation.src.utilities.dbUtility import DBUtility
import random

class CouponsDAO:

    def __init__(self):
        self.db_helper = DBUtility()

    def get_random_coupon_from_db(self, qty=1):
        """
        Gets a random coupon from db.
        :param qty: number of coupons to get
        :return:
        """

        sql = f"""SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
        WHERE post_type = 'shop_coupon' LIMIT 500;"""

        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(qty))

    def get_coupon_by_id(self, coupon_id):
        """
           Gets a coupon by ID from database.
           Parameters:
           coupon_id (str): ID of coupon to get
           Returns:
           list: database response.
        """

        sql = f'''SELECT * FROM {self.db_helper.database}.{self.db_helper.table_prefix}posts 
                  WHERE post_type = 'shop_coupon' AND ID = {coupon_id};'''

        return self.db_helper.execute_select(sql)

