import pandas as pd

def load_data(file_path):
    """
    CSV dosyasını yükler.
    :param file_path: str, dosyanın yolu
    :return: pandas.DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        print("Veri başarıyla yüklendi.")
        return df
    except Exception as e:
        print(f"Veri yüklenirken hata oluştu: {e}")
        return None

def clean_data(df):
    """
    Eksik ve hatalı verileri temizler.
    :param df: pandas.DataFrame
    :return: pandas.DataFrame
    """
    df = df.dropna()  # Eksik verileri kaldır
    df = df[df.applymap(lambda x: isinstance(x, (int, float, str)))]  # Geçersiz tipleri kaldır
    print("Veri temizleme işlemi tamamlandı.")
    return df

def transform_data(df):
    """
    Veriyi analiz için hazırlar.
    :param df: pandas.DataFrame
    :return: pandas.DataFrame
    """
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]  # Sütun adlarını düzenle
    print("Veri dönüştürüldü.")
    return df

def save_data(df, file_path):
    """
    İşlenmiş veriyi CSV olarak kaydeder.
    :param df: pandas.DataFrame
    :param file_path: str, kaydedilecek dosya yolu
    """
    df.to_csv(file_path, index=False)
    print(f"Veri kaydedildi: {file_path}")
