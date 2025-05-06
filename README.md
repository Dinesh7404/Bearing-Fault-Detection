# 🔧 Bearing Fault Detection using Deep Learning

🔗 **Live App**: [https://bearing-fault-detection.streamlit.app/](https://bearing-fault-detection.streamlit.app/)

This project detects bearing faults using advanced deep learning models. It utilizes vibration signal data and applies both **LSTM** and **CNN-LSTM** architectures to accurately identify different fault types.

---

## 🚀 Model Architectures

### 1. 🔁 LSTM Model

The **Long Short-Term Memory (LSTM)** network is built to analyze sequential vibration data and detect temporal patterns in signals.

- **Input Layer**: 9 statistical features  
- **LSTM Layers**: Multiple layers to capture time-based dependencies  
- **Dropout Layers**: Reduce overfitting  
- **Dense Layers**: Interpret and learn meaningful patterns  
- **Output Layer**: Probability distribution over fault classes  

### 2. 🧠 CNN-LSTM Model

The **CNN-LSTM** architecture merges **Convolutional Neural Networks** with **LSTM** to handle both spatial and temporal data characteristics.

- **Input Layer**: 9 statistical features  
- **CNN Layers**: Extract local and spatial patterns  
- **LSTM Layers**: Learn temporal trends  
- **Dense Layers**: Final fault classification  
- **Output Layer**: Probabilities of fault categories  

---

## ✅ Key Advantages

- **LSTM**: Excellent at capturing progressive deterioration in bearing performance.  
- **CNN-LSTM**: Combines spatial filtering (CNN) with sequence modeling (LSTM).  
- **Noise Robustness**: Both models perform well even with noisy vibration signals.  
- **Early Detection**: Capable of catching early-stage bearing faults.  

---

## 🏋️ Training Process

The models were trained on a large dataset of vibration signals collected from bearings in various conditions.

1. **Data Collection**: Real-world vibration data captured from different bearings.  
2. **Feature Extraction**: 9 time-domain statistical features calculated per sample.  
3. **Data Augmentation**: Noise injection to simulate real conditions and improve generalization.  
4. **Model Training**: Both models trained using backpropagation through time.  
5. **Validation**: Performance validated on unseen test sets.  
6. **Fine-Tuning**: Hyperparameters adjusted for maximum accuracy.  

---

## 📊 Results

Both models achieved **over 92% accuracy** on test data, demonstrating strong generalization and detection capabilities.

---

## 📂 Project Structure

