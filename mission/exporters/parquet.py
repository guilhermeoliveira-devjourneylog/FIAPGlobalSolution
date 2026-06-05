class ParquetExporter:

    @staticmethod
    def export(df, file):

        df.to_parquet(file)