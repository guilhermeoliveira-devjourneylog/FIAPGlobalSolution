class CSVExporter:

    @staticmethod
    def export(df, file):

        df.to_csv(
            file,
            index=False
        )