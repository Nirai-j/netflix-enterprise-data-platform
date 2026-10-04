from pathlib import Path


class FileWriter:

    @staticmethod
    def write_parquet(df, output_path):
        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        df.to_parquet(
            output_path,
            index=False
        )

        print(f"Saved: {output_path}")