class MyCrud:
    def __init__(self):
        import sqlite3 
        self.conexao = sqlite3.connect('moleza.db') 
        self.cursor = self.conexao.cursor()

    def fechardB (self):
        self.conexao.close()

    def criarTabela(self): 
        sql = """
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                nomes TEXT NOT NULL, 
                cpfs CHAR(11) NOT NULL
            );    
        """
        self.cursor.execute(sql)

    def inserir(self, nomes, cpfs):
        sql = """ 
        insert into pessoas (nomes, cpfs) 
        values (?, ?);
          """
        self.cursor.execute(sql, (nomes, cpfs)) 
        self.conexao.commit() 
        print ('Incluido com sucesso!')

    def ler(self):
        sql = 'select * from pessoas;' 
        result = self.cursor.execute(sql) 
        return result.fetchall()

    def alterar(self, id, nomes, cpfs): 
        sql = """
                update pessoas
                set nomes = ?, cpfs = ? 
                where id = ?;
            """
        self.cursor.execute(sql, (nomes, cpfs, id)) 
        self.conexao.commit() 
        print ('Modificado com sucesso!')

    def excluir(self, id):
        sql = 'delete from pessoas where id = ?;' 
        self.cursor.execute(sql, (id,))
        self.conexao.commit()
        print ('Excluido com sucesso!')