-- monthly_report.sql - Query Laporan Penjualan Bulanan

-- Query ini mengambil total pendapatan dan jumlah unit yang terjual
-- untuk setiap produk dalam bulan berjalan.

SELECT 
    t.product_id,
    p.product_name,
    SUM(t.quantity) AS total_sold,
    SUM(t.quantity * t.price) AS total_revenue
FROM 
    transactions t
JOIN 
    products p ON t.product_id = p.id
WHERE 
    t.transaction_date >= DATE_TRUNC('month', CURRENT_DATE)
GROUP BY 
    t.product_id, p.product_name
ORDER BY 
    total_revenue DESC;
