# 🤝 Hướng Dẫn Đóng Góp (Contributing Guide)

Cảm ơn bạn quan tâm đến dự án này! Hướng dẫn này sẽ giúp bạn tham gia phát triển.

---

## 📋 Mục Lục

1. [Trước Khi Bắt Đầu](#-trước-khi-bắt-đầu)
2. [Cách Đóng Góp](#-cách-đóng-góp)
3. [Code Standards](#-code-standards)
4. [Commit Messages](#-commit-messages)
5. [Pull Request Process](#-pull-request-process)
6. [Development Setup](#-development-setup)
7. [Testing](#-testing)
8. [Documentation](#-documentation)

---

## ✨ Trước Khi Bắt Đầu

### Đọc Tài Liệu

- [README.md](./README.md) - Hiểu project tổng quát
- [GETTING_STARTED.md](./GETTING_STARTED.md) - Quick start
- [DETAILED_INSTRUCTIONS](./INSTALLATION.md#-cài đặt) - cách cài đặt

### Hiểu Codebase

```
ai-agent-computer-use/
├── main.py           # Vòng lặp chính (OODA)
├── brain.py          # AI reasoning (G4F)
├── vision.py         # Screenshot & image processing
├── actions.py        # Mouse/keyboard control
├── server.py         # Web dashboard
├── config.py         # Global config
├── requirements.txt  # Dependencies
└── README.md         # Documentation
```

### Commit Lần Đầu

Fork dự án trước khi làm thay đổi:

```bash
# 1. Fork trên GitHub (click Fork button)

# 1. Fork repository trên GitHub (nhấn nút Fork)

# 2. Clone fork của bạn về máy
git https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use
cd AI-Agent-Computer-Use
git remote add upstream https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git


# 3. Thêm upstream để đồng bộ từ repo gốc
git remote add upstream https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git

# 4. Kiểm tra remote
git remote -v

# Kết quả mẫu:
# origin    https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git (fetch)
# origin    https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git (push)
# upstream  https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git (fetch)
# upstream  https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use.git (push)
```

---

## 🚀 Cách Đóng Góp

### Tìm Công Việc Cần Làm

Chọn một trong các cách:

1. **[Issues](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues)** - Bugs cần Fix hoặc features cần implement
2. **[Discussions](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/discussions)** - Ý tưởng mới
3. **Your own ideas** - Có ý tưởng của riêng bạn? Mở Issue trước!

### Các Loại Đóng Góp

#### 1️⃣ Bug Fixes

```bash
# Tạo branch
git checkout -b Fix/bug-description
# Ví dụ: Fix/agent-click-coordinates

# Fix bug
# ... edit files ...

# Commit
git commit -m "Fix: [module] description of Fix"
```

#### 2️⃣ New Features

```bash
# Tạo branch
git checkout -b feature/new-feature-name
# Ví dụ: feature/voice-control

# Implement feature
# ... add new files/code ...

# Commit
git commit -m "Feat: [module] description of feature"
```

#### 3️⃣ Documentation

```bash
# Tạo branch
git checkout -b docs/doc-name
# Ví dụ: docs/api-reference

# Thêm/sửa documentation
# ... update README, create guides ...

# Commit
git commit -m "Docs: description of changes"
```

#### 4️⃣ Tests

```bash
# Tạo branch
git checkout -b test/test-name
# Ví dụ: test/brain-module

# Viết tests
# ... create test files ...

# Commit
git commit -m "Test: [module] description"
```

#### 5️⃣ Refactoring / Optimization

```bash
# Tạo branch
git checkout -b refactor/refactor-name
# Ví dụ: refactor/vision-module

# Refactor code
# ... improve code quality ...

# Commit
git commit -m "Refactor: [module] description"
```

---

## 📝 Code Standards

### Python Style Guide (PEP 8)

```python
# ✓ DO THIS

def move_mouse(x: int, y: int) -> None:
    """
    Di chuyển chuột đến vị trí (x, y) một cách mượt mà.
    
    Args:
        x: Tọa độ X (pixels)
        y: Tọa độ Y (pixels)
    """
    # Validate input
    x = max(0, min(x, config.SCREEN_WIDTH - 1))
    y = max(0, min(y, config.SCREEN_HEIGHT - 1))
    
    # Thực hiện action
    pyautogui.moveTo(x, y, duration=config.MOUSE_MOVE_DURATION)


# ✗ DON'T DO THIS

def move_mouse(x,y):
    pyautogui.moveTo(x,y)
```

### Checklist Trước Submit

- [ ] **Type hints**: Tất cả functions có type hints
- [ ] **Docstrings**: Tất cả functions/classes có docstrings
- [ ] **Comments**: Code phức tạp có comments giải thích
- [ ] **PEP 8**: Code follow PEP 8 style
- [ ] **No hardcoded values**: Dùng config.py
- [ ] **Error handling**: Try-catch khi cần
- [ ] **Logging**: Debug logs cho actions quan trọng

### Naming Conventions

```python
# Variables - snake_case
screenshot_count = 0
is_success = True

# Functions - snake_case
def capture_screen():
    pass

def analyze_and_decide():
    pass

# Classes - PascalCase
class Brain:
    pass

class Vision:
    pass

# Constants - UPPER_SNAKE_CASE
MAX_STEPS = 30
SCREEN_WIDTH = 1920

# Private - leading underscore
def _internal_method():
    pass

def _private_helper():
    pass
```

### Import Organization

```python
# 1. Standard library
import os
import sys
import time
from typing import Optional
from datetime import datetime

# 2. Third-party
import pyautogui
import g4f
from flask import Flask

# 3. Local
from brain import Brain
from vision import Vision
import config
```

---

## 💬 Commit Messages

### Format

```
[Type]: [Module] Brief description

Detailed explanation of changes (if needed)

Fixes #issue_number
Related to #related_issues
```

### Types

- `Fix:` - Bug Fix
- `Feat:` - New feature
- `docs:` - Documentation
- `test:` - Tests
- `refactor:` - Code refactoring
- `perf:` - Performance improvement
- `chore:` - Build, deps, config

### Examples

```bash
# Good commits
git commit -m "Fix: brain - handle G4F provider timeout"
git commit -m "Feat: vision - add support for multi-screen"
git commit -m "docs: readme - add Vietnamese translation"
git commit -m "test: actions - add unit tests for mouse control"
git commit -m "refactor: config - organize settings by category"
git commit -m "perf: vision - optimize screenshot compression"

# Bad commits
git commit -m "fixed bug"
git commit -m "update"
git commit -m "asdf"
```

### Atomicity

```bash
# ✓ Good - Logical commits
git commit -m "Feat: vision - add grid overlay to screenshots"
git commit -m "docs: vision - add grid documentation"

# ✗ Bad - Too many things in one commit
git commit -m "fixed vision, updated docs, added tests, optimized brain"
```

---

## 🔄 Pull Request Process

### Bước 1: Sync với Main Repository

```bash
# Fetch latest changes
git fetch upstream

# Rebase trên main
git rebase upstream/main

# Push lên fork
git push origin feature/name -f
```

### Bước 2: Tạo Pull Request

1. Vào GitHub → fork của bạn
2. Click "Compare & pull request"
3. Fill in PR template:

```markdown
## Description
Mô tả thay đổi của bạn

## Type of Change
- [ ] Bug Fix (Fix without breaking changes)
- [ ] New feature (new feature without breaking changes)
- [ ] Breaking change (Fix or feature causing breaking changes)
- [ ] Documentation

## How Has This Been Tested?
Describe the tests you ran and how to reproduce them.

## Testing Checklist
- [ ] Tested on Windows
- [ ] Tested on macOS
- [ ] Tested on Linux
- [ ] No new errors or warnings

## Documentation Checklist
- [ ] Updated README if needed
- [ ] Added comments for complex code
- [ ] Added docstrings to new functions

## Related Issues
Fixes #issue_number
Related to #related_issues

## Additional Notes
Anything else reviewers should know?
```

### Bước 3: Code Review

- Maintainers sẽ review code
- Respond to comments & make requested changes
- Push thêm commits (không need to rebase)
- Request re-review

### Bước 4: Merge

Sau khi approved:
- Squash & merge (nếu nhiều commits)
- Delete branch khi merged

---

## 🔧 Development Setup

### Install Dev Dependencies

```bash
# Create venv
python -m venv .venv
source .venv/bin/activate 

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate 

# Install requirements
pip install -r requirements.txt

# Install dev requirements (nếu có)
pip install -r requirements-dev.txt

# Install linting/formatting tools
pip install black flake8 pytest pylint
```

### Setup Pre-commit Hooks (Optional)

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black
        
  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
        args: [--max-line-length=120]
EOF

# Install hooks
pre-commit install
```

### Development Workflow

```bash
# 1. Create branch
git checkout -b feature/my-feature

# 2. Make changes
# ... edit files ...

# 3. Format code
black .
flake8 .

# 4. Test
pytest tests/

# 5. Commit
git add .
git commit -m "Feat: my awesome feature"

# 6. Push
git push origin feature/my-feature

# 7. Create PR on GitHub
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_brain.py -v

# Run specific test
pytest tests/test_brain.py::test_analyze_screenshot -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html
```

### Write Tests

**Ví dụ: `tests/test_actions.py`**

```python
import pytest
from actions import Actions
import pyautogui

class TestActions:
    """Tests for Actions module"""
    
    @pytest.fixture
    def actions(self):
        """Setup fixture"""
        return Actions()
    
    def test_move_mouse_valid(self, actions):
        """Test moving mouse to valid coordinates"""
        # Arrange
        x, y = 100, 200
        
        # Act
        actions.move_mouse(x, y)
        
        # Assert - xem xét current mouse position
        # (Trong thực tế, khó assert mouse position, nên có thể skip)
        assert actions.action_count > 0
    
    def test_move_mouse_boundaries(self, actions):
        """Test mouse stays within screen boundaries"""
        # Arrange
        x, y = 99999, 99999
        
        # Act
        actions.move_mouse(x, y)
        
        # Assert
        # Mouse should be clamped to valid range
        assert True  # Passed if no exception
    
    def test_type_text_unicode(self, actions):
        """Test typing unicode text (Vietnamese)"""
        # Arrange
        text = "Xin chào"
        
        # Act
        actions.type_text(text)
        
        # Assert
        assert actions.action_count > 0
```

### Test Coverage

```bash
# Generate coverage report
pytest tests/ --cov=. --cov-report=html

# Windows
start htmlcov/index.html

# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html
```

---

## 📚 Documentation

### Update README

Nếu thêm feature lớn, update README.md:

```markdown
## My New Feature

Brief description...

### Usage

```python
# Code example
```

### Configuration

- Setting 1: description
- Setting 2: description
```

### Add Examples

Thêm file trong `examples/`:

```bash
# Tạo example file
cat > examples/my_example.py << 'EOF'
"""
Example: Description of what this does

Usage:
    python examples/my_example.py
"""

# Code here
EOF
```

### Add API Documentation

Nếu thêm public function:

```python
def new_function(arg1: str, arg2: int) -> dict:
    """
    Brief description (one line).
    
    Longer description if needed (multiple lines).
    
    Args:
        arg1: Description of arg1
        arg2: Description of arg2 (type: int, range: 0-100)
    
    Returns:
        dict: Description of return value
            {
                'success': bool,
                'data': str
            }
    
    Raises:
        ValueError: If arg2 is out of range
        TimeoutError: If operation takes too long
    
    Example:
        >>> result = new_function("test", 50)
        >>> print(result['success'])
        True
    
    Note:
        - This function requires internet connection
        - Returns cached result if called within 5 minutes
    """
    pass
```

---

## 🎯 Feature Request Process

Muốn thêm feature mới?

### 1. Check Issues

Cek [Issues](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues) xem đã có ai propose không.

### 2. Mở Issue

```markdown
## Feature Request: [Title]

### Description
Mô tả feature bạn muốn add

### Use Case
Giải thích tại sao cần feature này?

### Proposed Solution
Làm sao implement?

### Alternatives Considered
Có cách nào khác không?

### Additional Context
Thông tin khác?
```

### 3. Discuss

- Đợi maintainers comment
- Decide cách implement
- Design trước khi code

### 4. Implement

- Follow development process ở trên
- Create PR khi ready

---

## 🐛 Bug Report Process

Tìm bug?

### 1. Check Issues

Xem [Issues](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/issues) đã report chưa.

### 2. Mở Issue

```markdown
## Bug Report: [Title]

### Description
Mô tả bug

### Steps to Reproduce
1. ...
2. ...
3. ...

### Expected Behavior
Cái gì diễn ra bình thường?

### Actual Behavior
Cái gì diễn ra sai?

### Environment
- OS: Windows 10 / macOS 12 / Ubuntu 22.04
- Python: 3.10.5
- Browser: Chrome 120 (if relevant)
- Config: any custom config?

### Screenshots/Logs
Attach ảnh, logs, error messages

### Possible Solution
Bạn có ý tưởng Fix không?
```

### 3. Help Fix

- Comment trên issue
- Đề xuất solution
- Create PR nếu bạn Fix được

---

## 📞 Communication

### Channels

- **Issues**: Bug reports & feature requests
- **Discussions**: Ý tưởng, questions, announcements
- **Pull Requests**: Code reviews
- **Email**: Gửi private message nếu cần (check README)

### Code of Conduct

- Tôn trọng tất cả contributors
- Mở ra với ý kiến khác
- Focus vào code, không attack người
- Help others, be patient

---

## 🎓 Resources

### Learning

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python](https://realpython.com/)

### Tools

- **Black**: Auto code formatter
- **Flake8**: Linter
- **Pytest**: Testing framework
- **Coverage.py**: Test coverage

### Git

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## ✅ Checklist Trước Submit PR

## ✅ Pull Request Checklist

- [ ] Forked the repository and created a new branch
- [ ] Code changes completed and tested
- [ ] Code formatted successfully (`black .`)
- [ ] Lint checks passed (`flake8 .`)
- [ ] Tests added/updated and passing (`pytest`)
- [ ] Docstrings added for new functions/classes
- [ ] Comments added where necessary
- [ ] README or documentation updated if required
- [ ] No breaking changes introduced (or discussed beforehand)
- [ ] Commit messages follow project conventions
- [ ] Pull Request description completed
- [ ] Related issues linked (`Fixes #123`)

---

## 🎉 Cảm Ơn!

Cảm ơn bạn đóng góp cho dự án! 

Bất kỳ câu hỏi nào:
- Mở [Discussion](https://github.com/khoadeptrai030-cmyk/AI-Agent-Computer-Use/discussions)
- Comment trên Issue
- Email maintainers

**Happy Contributing! 🚀**
