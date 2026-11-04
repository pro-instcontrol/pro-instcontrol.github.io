# -*- coding: utf-8 -*-
"""Handbook Chapter 84 — Applied Intelligence Processing (Xử lý thông minh ứng dụng).
Run:  python build/reader_hb_ch84.py
"""
import os
import hb_common as C
from hb_common import p, h2, h3, eq, table

CSLUG = 'ch84-applied-intelligence-processing'
CH_NO = 84
TITLE_EN = 'Applied Intelligence Processing'
TITLE_VI = 'Xử lý thông minh ứng dụng'
BYLINE = "John G. Webster (chủ biên) · CRC Press, 1999"
FIGS = {}


def body_vi():
    b = []
    b.append(p('Xử lý thông minh biến dữ liệu cảm biến thô thành quyết định: hiệu chuẩn tự động, hợp nhất đa cảm biến, ước lượng trạng thái, nhận dạng mẫu, phát hiện bất thường và bảo trì dự báo. Các công cụ trải từ lọc Kalman cổ điển đến mạng nơ-ron và suy luận mờ.'))
    b.append(p('Khác với xử lý tín hiệu thuần tuý, lớp này làm việc trên đặc trưng và ngữ cảnh, nên yêu cầu dữ liệu huấn luyện đại diện, quản lý khái niệm trôi và khả năng giải thích kết quả trong các ứng dụng an toàn.'))
    b.append(h2('84.1 Hợp nhất cảm biến và lọc Kalman', 'Sensor Fusion and Kalman Filtering'))
    b.append(p('Hợp nhất kết hợp các nguồn đo bổ trợ (IMU + GNSS, nhiệt độ + áp suất + rung) để giảm nhiễu, mở rộng băng thông và tăng độ tin cậy khi một cảm biến hỏng. Lọc Kalman là ước lượng bình phương trung bình nhỏ nhất theo hai bước dự báo – cập nhật, trọng số hoá theo hiệp phương sai của mô hình và của phép đo; biến thể EKF/UKF xử lý mô hình phi tuyến.'))
    b.append(eq('x̂⁻_k = F x̂_{k−1} + Bu_k ,   K_k = P⁻_k Hᵀ(HP⁻_k Hᵀ + R)⁻¹ ,   x̂_k = x̂⁻_k + K_k(z_k − Hx̂⁻_k)', '84.1'))
    b.append(h2('84.2 Trích xuất đặc trưng và giảm chiều', 'Feature Extraction and Dimensionality Reduction'))
    b.append(p('Từ tín hiệu thô rút đặc trưng thời gian (RMS, kurtosis, crest factor), tần số (năng lượng dải, tần số đỉnh), thời–tần (STFT, wavelet, envelope). PCA chiếu dữ liệu lên các trục phương sai lớn nhất để giảm chiều và khử tương quan; lựa chọn đặc trưng và chuẩn hoá (z-score) quyết định hiệu năng của bộ phân loại hơn là độ phức tạp của mô hình.'))
    b.append(eq('z = (x − µ)/σ ,   C = (1/(n−1))XᵀX ,   C·v_i = λ_i·v_i   (PCA)', '84.2'))
    b.append(h2('84.3 Phân loại, mờ và phát hiện bất thường', 'Classification, Fuzzy Logic and Anomaly Detection'))
    b.append(p('Bộ phân loại (k-NN, SVM, cây quyết định, mạng nơ-ron tích chập cho ảnh và phổ) gán nhãn trạng thái thiết bị. Logic mờ và hệ chuyên gia mã hoá tri thức vận hành dưới dạng luật khi ngưỡng cứng không phù hợp. Phát hiện bất thường dùng khoảng cách Mahalanobis, autoencoder hoặc isolation forest so với đường nền học được; cảnh báo sai (false alarm) phải được kiểm soát bằng ngưỡng thích ứng.'))
    b.append(table(['Nhiệm vụ', 'Phương pháp', 'Đầu ra', 'Lưu ý triển khai'], [['Ước lượng trạng thái', 'Kalman / EKF / UKF', 'Trạng thái + hiệp phương sai', 'Cần mô hình nhiễu Q, R'], ['Hợp nhất', 'Trọng số / Bayes / D–S', 'Giá trị tin cậy hơn', 'Đồng bộ thời gian'], ['Giảm chiều', 'PCA / LDA', 'Đặc trưng cô đọng', 'Chuẩn hoá bắt buộc'], ['Phân loại lỗi', 'SVM / CNN / cây', 'Nhãn trạng thái', 'Dữ liệu lỗi hiếm'], ['Bất thường', 'Autoencoder / Mahalanobis', 'Điểm bất thường', 'Khái niệm trôi'], ['Tri thức vận hành', 'Logic mờ / luật', 'Quyết định giải thích được', 'Bảo trì luật']], 'Bảng 84.1 · Các lớp xử lý thông minh trong đo lường.'))
    b.append(h2('84.4 Triển khai biên và độ tin cậy', 'Edge Deployment and Trust'))
    b.append(p('Suy luận tại biên (edge AI) giảm độ trễ và băng thông nhưng đòi hỏi lượng tử hoá mô hình (int8), quản lý bộ nhớ và giám sát trôi dữ liệu. Với hệ đo an toàn chức năng, cần giữ một đường chẩn đoán độc lập, ghi nhật ký quyết định và kiểm chứng độ bao phủ của tập huấn luyện trước khi cấp phép.'))
    b.append(h2("Tóm tắt", "Summary"))
    b.append(p('Lớp thông minh gồm hợp nhất/ước lượng (Kalman: dự báo rồi cập nhật theo K_k), trích xuất đặc trưng và PCA, phân loại/mờ/phát hiện bất thường, triển khai biên. Chất lượng dữ liệu, đồng bộ thời gian, chuẩn hoá và giám sát khái niệm trôi quan trọng hơn độ sâu mô hình.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Mục lục</span>Sổ tay</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Mục lục →</span>Sổ tay</a></div>'
             % (C.BASE_VI, C.BASE_VI))
    return "".join(b)


def body_en():
    b = []
    b.append(p('Companion to the Vietnamese translation of Chapter 84. The source prose is not repeated; the governing relations and reference data are summarised below.'))
    b.append(p('Intelligent processing turns sensor data into decisions: multi-sensor fusion and Kalman/EKF/UKF state estimation (predict–update with gain K from P and R), time/frequency/time–frequency feature extraction, PCA whitening, classifiers (SVM, CNN), fuzzy rule bases and unsupervised anomaly detection (autoencoders, Mahalanobis distance, isolation forests). Practical reliability depends on representative training data, z-score normalisation, time synchronisation, concept-drift monitoring and an independent diagnostic path for safety-related measurements. Edge deployment adds int8 quantisation and latency/memory constraints.'))
    b.append(eq('x̂⁻_k = F x̂_{k−1} + Bu_k ,   K_k = P⁻_k Hᵀ(HP⁻_k Hᵀ + R)⁻¹ ,   x̂_k = x̂⁻_k + K_k(z_k − Hx̂⁻_k)', '84.1'))
    b.append(eq('z = (x − µ)/σ ,   C = (1/(n−1))XᵀX ,   C·v_i = λ_i·v_i   (PCA)', '84.2'))
    b.append(table(['Task', 'Method', 'Output', 'Deployment note'], [['State estimation', 'Kalman / EKF / UKF', 'State + covariance', 'Tune Q and R'], ['Fusion', 'Weighted / Bayes / D–S', 'More reliable value', 'Time synchronisation'], ['Reduction', 'PCA / LDA', 'Compact features', 'Normalisation mandatory'], ['Fault classification', 'SVM / CNN / trees', 'State label', 'Scarce fault data'], ['Anomaly detection', 'Autoencoder / Mahalanobis', 'Anomaly score', 'Concept drift'], ['Operator knowledge', 'Fuzzy / rule base', 'Explainable decision', 'Rule maintenance']], 'Table 84.1 · Intelligent-processing layers in instrumentation.'))
    b.append('<div class="chapter-nav">'
             '<a href="%s"><span class="k">← Contents</span>Handbook</a>'
             '<a href="%s" style="text-align:right;"><span class="k">Contents →</span>Handbook</a></div>'
             % (C.BASE_EN, C.BASE_EN))
    return "".join(b)


def main():
    for path in C.write_chapter(CH_NO, CSLUG, TITLE_EN, TITLE_VI, BYLINE,
                                body_vi(), body_en(), FIGS):
        print("wrote %s  %d kB" % (path, os.path.getsize(path) // 1024))


if __name__ == "__main__":
    main()
