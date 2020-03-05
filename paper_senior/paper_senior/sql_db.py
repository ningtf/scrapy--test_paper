'''
操作mysql的工具类
功能:
1. 获取连接
2. CURD(增删改查)独立公用的方法
'''
import pymysql
class SqlDb(object):
    #构造方法,初始化对象信息
    def __init__(self, host,db,user,password):
        self.host =host
        self.db = db
        self.user= user
        self.password = password
        self.charset='utf8'
    #获得连接
    def get_conn(self):
        conn = pymysql.connect(host=self.host,
                               port=3306,db=self.db,
                               user=self.user,
                               password=self.password)
        return conn
    def my_fetchall(self,sql,canshu):
        '''
                            查询
        '''
        conn = self.get_conn()
        cursor = conn.cursor()
        if canshu=="":
            cursor.execute(sql)
        else:
            cursor.execute(sql,canshu)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    def execute_sql(self,sql,canshu):
        '''
                            非查询(增删改)
        '''
        try:
            conn = self.get_conn()
            cursor = conn.cursor()
            num = cursor.execute(sql,canshu)
            conn.commit()
            cursor.close()
            conn.close()
            return num
        except:
            conn.rollback()
 
            return 0
      
    def  md5_jiami(self):
        pass
    
# if __name__ == '__main__':
#     db_mysql = SqlDb('127.0.0.1','qingyou','root','root')
#     print(db_mysql.get_conn())
    # 增删改
    # sql= "insert into xiaohua(id,content) values(default,%s)"
    # canshu=['笑话2222']
    # sql= "delete from xiaohua where id= %s"
    # canshu=['2']
    # num = db_mysql.execute_sql(sql, canshu)
    # if num >0:
    #     print('执行成功')
    # else:
    #     print("执行失败")
    
    
    
    
    