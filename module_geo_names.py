class geo_name:
    
    def bd_connect(host = '127.0.0.1', username = 'postgres', password = '123', database = 'mybd', port = 5432, drivername = 'postgresql'):
        from sqlalchemy import create_engine
        from sqlalchemy.engine.url import URL
        DATABASE = {
        'drivername': drivername,
        'username': username, 
        'password': password, 
        'host': host,
        'port': port,
        'database': database,
        'query': {}
        }  
        return create_engine(URL(**DATABASE))



    @staticmethod
    def vectorization(model, cities_list, replace_or_append_or_nan = 'nan'):
        import pandas as pd
        embeddings = model.encode(cities_list)
        if replace_or_append_or_nan == 'nan':
            return embeddings
        elif replace_or_append_or_nan == 'replace':
            embeddings_df = pd.DataFrame(embeddings)
            embeddings_df.to_sql('embeddings', con = geo_name.bd_connect(), if_exists = 'replace')
        elif replace_or_append_or_nan == 'replace':
            embeddings_df = pd.DataFrame(embeddings)
            embeddings_df.to_sql('embeddings', con = geo_name.bd_connect(), if_exists = 'append')           
        return embeddings
