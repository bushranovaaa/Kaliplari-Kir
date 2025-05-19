# main_algorithm.py
import os
from data_processing import load_data, clean_data, transform_data, analyze_data, save_data

# 1. Ana algoritma fonksiyonu
def run_algorithm(input_file, output_file):
    """
    Temel algoritma akışını çalıştırır.
    
    Args:
    input_file (str): Girdi verisinin dosya yolu
    output_file (str): İşlenmiş verinin kaydedileceği dosya yolu
    
    Returns:
    None
    """
    # 2. Veriyi yükle
    print("Loading data...")
    data = load_data(input_file)
    
    # 3. Veriyi temizle
    print("Cleaning data...")
    cleaned_data = clean_data(data)
    
    # 4. Veriyi dönüştür
    print("Transforming data...")
    transformed_data = transform_data(cleaned_data)
    
    # 5. Veriyi analiz et
    print("Analyzing data...")
    analyze_data(transformed_data)
    
    # 6. Sonuçları kaydet
    print(f"Saving processed data to {output_file}...")
    save_data(transformed_data, output_file)

# 2. Ana fonksiyonu çalıştır
if __name__ == '__main__':
    # Girdi ve çıktı dosya yolları
    input_file = 'data.csv'  # Buraya veri dosyanızın yolunu yazın
    output_file = 'processed_data.csv'  # Buraya çıktı dosyasının yolunu yazın
    
    # Algoritmayı çalıştır
    run_algorithm(input_file, output_file)
