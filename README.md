# learn-dspy

Dự án học cách sử dụng DSPy - một framework giúp tối ưu hóa prompts và weights của Language Models một cách tự động.

## 🚀 Giới thiệu

DSPy là một framework Python cho phép bạn:
- Xây dựng các chương trình với Language Models một cách có cấu trúc
- Tự động tối ưu hóa prompts thông qua compilation
- Tạo các pipeline phức tạp với syntax Pythonic đơn giản

## 📋 Yêu cầu

- Python 3.12 trở lên
- uv (để quản lý môi trường và dependencies)

## ⚙️ Cài đặt

### 1. Cài đặt uv (nếu chưa có)

```bash
# macOS và Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Hoặc dùng pip
pip install uv
```

### 2. Clone repository và cài đặt dependencies

```bash
git clone https://github.com/TaQuangKhoi/learn-dspy.git
cd learn-dspy

# uv sẽ tự động tạo virtual environment và cài đặt dependencies
uv sync
```

### 3. Cấu hình API Keys

Sao chép file `.env.example` thành `.env` và điền API keys của bạn:

```bash
cp .env.example .env
# Sau đó chỉnh sửa file .env với API key của bạn
```

**Lưu ý:** Để lấy OpenAI API key, truy cập: https://platform.openai.com/api-keys

## 🎯 Các ví dụ có sẵn

### 1. Basic Example - Ví dụ cơ bản

Học cách định nghĩa Signature và Predictor cơ bản:

```bash
uv run python examples/basic.py
# Hoặc
./run-basic.sh
```

### 2. QA System - Hệ thống hỏi đáp

Xây dựng hệ thống hỏi đáp với Chain-of-Thought:

```bash
# Cần có OPENAI_API_KEY trong .env
uv run python examples/qa_system.py
# Hoặc
./run-qa.sh
```

### 3. RAG Example - Retrieval-Augmented Generation

Tìm hiểu cách xây dựng hệ thống RAG đơn giản:

```bash
# Cần có OPENAI_API_KEY trong .env
uv run python examples/rag_example.py
# Hoặc
./run-rag.sh
```

## 📁 Cấu trúc dự án

```
learn-dspy/
├── examples/           # Các ví dụ học DSPy
│   ├── __init__.py
│   ├── basic.py       # Ví dụ cơ bản
│   ├── qa_system.py   # Hệ thống QA
│   └── rag_example.py # RAG system
├── .env.example       # Template cho environment variables
├── pyproject.toml     # Cấu hình dự án và dependencies
├── README.md          # File này
└── main.py           # Entry point chính
```

## 🔧 Chạy các ví dụ theo cách khác

### Xem danh sách ví dụ

```bash
uv run python main.py
```

### Sử dụng uv run trực tiếp

```bash
# Chạy file Python trực tiếp
uv run python examples/basic.py
uv run python examples/qa_system.py
uv run python examples/rag_example.py
```

### Sử dụng shell scripts

```bash
./run-basic.sh
./run-qa.sh
./run-rag.sh
```

### Sử dụng virtual environment thủ công

```bash
# Kích hoạt virtual environment
source .venv/bin/activate  # Linux/macOS
# hoặc
.venv\Scripts\activate     # Windows

# Chạy examples
python examples/basic.py
python examples/qa_system.py
python examples/rag_example.py
```

## 📚 Tài liệu tham khảo

- [DSPy Documentation](https://dspy-docs.vercel.app/)
- [DSPy GitHub](https://github.com/stanfordnlp/dspy)
- [uv Documentation](https://docs.astral.sh/uv/)

## 💡 Mẹo

1. **Không có OpenAI API key?** Bạn có thể sử dụng local models với Ollama:
   ```bash
   # Cài đặt Ollama: https://ollama.ai
   # Tải model: ollama pull llama2
   # Sau đó sửa code để dùng: dspy.LM('ollama/llama2', api_base='http://localhost:11434')
   ```

2. **Chạy nhanh một ví dụ:** 
   ```bash
   uv run python examples/basic.py
   # hoặc
   ./run-basic.sh
   ```

3. **Thêm dependencies mới:**
   ```bash
   uv add package-name
   ```

4. **Xem dependencies hiện tại:**
   ```bash
   uv pip list
   ```

5. **Cập nhật dependencies:**
   ```bash
   uv sync
   ```

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📝 License

Apache License 2.0 - Xem file [LICENSE](LICENSE) để biết thêm chi tiết.
