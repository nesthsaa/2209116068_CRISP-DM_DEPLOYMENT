import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Dashboard Tren Pembelian Kacamata di Amazon')


# Fungsi untuk menampilkan plot menggunakan Seaborn
def show_countplot(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='stars', data=df, palette='Set2')
    plt.title('Rating yang Paling Banyak Diterima')
    plt.xlabel('Rating')
    plt.ylabel('Jumlah Produk')

    # Simpan objek gambar
    fig = plt.gcf()
    
    # Tampilkan plot menggunakan st.pyplot() dengan menyertakan objek gambar
    st.pyplot(fig)

# Main function
def main():
    # Load data
    df = pd.read_csv("best_sellers_amazon_2024_sunglasses.csv")  # Ganti "your_dataset.csv" dengan nama file dataset Anda
    # Tampilkan plot
    st.header("Rating yang Paling Banyak Diterima")
    show_countplot(df)
     # Tampilkan penjelasan
    st.write("Grafik di atas menunjukkan jumlah produk kacamata dari setiap rating.\n"
             "Berdasarkan grafik, dapat dilihat bahwa rating 4,5 adalah rating yang paling banyak diterima dengan hampir 70 produk yang mendapatkan rating tersebut.\n"
             "Sedangkan rating 3,8 dan 3,9 adalah rating yang paling sedikit diterima")

if __name__ == "__main__":
    main()




# Fungsi untuk menampilkan Daftar Merk Kacamata Berdasarkan Rating
# Main function
def main():
    
    # Load data
    df = pd.read_csv("Data Cleaned.csv")  # Ganti "your_dataset.csv" dengan nama file dataset Anda
    
    # Filter rating yang tersedia
    available_ratings = sorted(df['stars'].unique())
    
    # Pilih rating yang akan ditampilkan
    selected_rating = st.sidebar.selectbox("Pilih Rating:", available_ratings)

    st.header("Daftar Merk Kacamata Berdasarkan Rating")
    st.write(" User dapat memilih rating kacamata yang ingin mereka lihat, dan kemudian sistem akan menampilkan daftar merek kacamata yang memiliki rating tersebut.")
    st.subheader(f"Jumlah Kacamata untuk Rating {selected_rating}")
    filtered_df = df[df['stars'] == selected_rating]
    st.write(filtered_df)
    st.write("Total produk:", len(filtered_df))
    st.write("Merek yang dibeli:", filtered_df['brand'].unique())

if __name__ == "__main__":
    main()



#Fungsi untuk menampilkan Persebaran Kacamata Berdasarkan Rating
# Main function
def main():
    st.header("Persebaran Kacamata Berdasarkan Rating")
    
    # Load data
    df = pd.read_csv("encoded.csv")  # Ganti "your_dataset.csv" dengan nama file dataset Anda
    
    # Ubah nilai StarsCategory menjadi label yang sesuai
    df['StarsCategory'] = df['StarsCategory'].map({0: 'Rendah', 1: 'Baik', 2: 'Tinggi'})
    
    # Hitung jumlah kacamata berdasarkan StarsCategory
    counts = df['StarsCategory'].value_counts()
    
    # Visualisasi menggunakan barplot dengan warna yang disesuaikan
    plt.figure(figsize=(8, 6))
    sns.barplot(x=counts.index, y=counts.values, color='#FF69B4')  # Ganti warna menjadi 'skyblue'
    plt.title('Persebaran Kacamata Berdasarkan Rating')
    plt.xlabel('Rating')
    plt.ylabel('Jumlah Kacamata')
    st.pyplot(plt)
    st.write("Grafik di atas menunjukkan bahwa rating yang paling banyak dipilih adalah rating dengan kategori Tinggi.\n"
             "Terdapat lebih dari 160 kacamata yang mendapat rating ini. Selanjutnya terdapat kategori rating Baik dengan lebih dari 60 kacamata yang mendapat rating ini\n"
             "Rating Rendah memiliki jumlah kacamata yang paling sedikit. Tidak lebih dari 10 kacamata yang mendapat rating Rendah.")

if __name__ == "__main__":
    main()



# Fungsi untuk menampilkan Perbandingan antara Rating dan Harga
# Main function
def main():

    # Load data
    df = pd.read_csv("Data Cleaned.csv")

    # Ubah nilai StarsCategory menjadi label yang sesuai
    df['StarsCategory'] = df['StarsCategory'].map({0: 'Rendah', 1: 'Baik', 2: 'Tinggi'})
    
    # Hitung rata-rata harga berdasarkan kategori bintang
    avg_price_by_stars = df.groupby('StarsCategory')['price/value'].mean().reset_index()
    
    # Temukan kategori bintang dengan rata-rata harga tertinggi
    max_avg_price_category = avg_price_by_stars.loc[avg_price_by_stars['price/value'].idxmax(), 'StarsCategory']
    
    # Perbandingan: Bar Chart
    st.header("Perbandingan Data Rating dan Harga")
    fig, ax = plt.subplots()
    
    # Tentukan warna bar untuk nilai paling signifikan
    palette = ['grey' if cat != max_avg_price_category else '#FF69B4' for cat in avg_price_by_stars['StarsCategory']]
    
    sns.barplot(x='StarsCategory', y='price/value', data=avg_price_by_stars, palette=palette, ax=ax)
    ax.set_title('Perbandingan antara Rating dan Harga')
    ax.set_xlabel('Kategori Rating')
    ax.set_ylabel('Harga / Nilai')
    
    st.pyplot(fig)
    st.write("Diagram di atas menunjukkan bahwa rating dengan kategori tinggi memiliki harga yang lebih mahal dibanding kategori lainnya.\n"
             "Secara umum, terdapat korelasi positif antara rating dan harga. Artinya, produk dengan rating lebih tinggi cenderung lebih mahal daripada produk dengan rating lebih rendah.")

if __name__ == "__main__":
    main()



# Fungsi untuk menampilkan Top 5 Produk Terlaris
# Main function
def main():
    
    # Load data
    df = pd.read_csv("best_sellers_amazon_2024_sunglasses.csv")
    
    # Hitung jumlah pembelian untuk setiap merek
    top_brand = df['brand'].value_counts().head(5)
    
    # Tampilkan visualisasi produk terlaris dalam bentuk pie chart
    st.header("Produk Terlaris")
    fig, ax = plt.subplots()
    ax.pie(top_brand, labels=top_brand.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Memastikan pie chart terlihat seperti lingkaran
    plt.title('Top 5 Produk Terlaris')
    st.pyplot(fig)
    st.write("Grafik di atas menunjukkan menunjukkan persentase 5 brand kacamata terlaris. Sojos menjadi brand terlaris dengan 32.2% produk yang terjual, diikuti oleh Ray-Ban dengan 30.5%, Oakley 16.9%, Kaliyadi 11.9%, dan Rockbros 8.5%,")

if __name__ == "__main__":
    main()



# Fungsi untuk menampilkan 5 Produk dengan Penjualan Rendah
# Main function
def main():
    
    # Load data 
    df = pd.read_csv("best_sellers_amazon_2024_sunglasses.csv")
    
    # Hitung jumlah pembelian untuk setiap merek
    low_sales_brand = df['brand'].value_counts().tail(5)  # Mengambil 5 merek dengan penjualan terendah
    
    # Tampilkan visualisasi produk dengan penjualan rendah dalam bentuk pie chart
    st.header("Produk dengan Penjualan Ter-Rendah")
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(low_sales_brand, labels=low_sales_brand.index, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Memastikan pie chart terlihat seperti lingkaran
    plt.title('5 Produk dengan Penjualan Ter-Rendah')
    
    # Menampilkan angka langsung di dalam setiap bagian pie
    for i, val in enumerate(low_sales_brand):
        autotexts[i].set_text(f"{val}")
    
    st.pyplot(fig)
    st.write("Grafik di atas menunjukkan 5 brand kacamatan dengan penjualan terendah, dimana produk yang berhasil terjual dari kelima brand ini hanyalah satu")

if __name__ == "__main__":
    main()