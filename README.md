# FastAPI Demo

一个简单的FastAPI演示项目，包含POST API接口和Docker容器化部署。

## 功能特性

- 提供POST API接口 `/hello`，接收name参数并返回问候语
- 使用Docker容器化部署
- 支持GitHub Actions自动构建并推送镜像到DockerHub

## API文档
`http://localhost:8000/docs`

## API接口

### POST /hello
接收name参数，返回问候语。

**请求示例：**
```bash
curl -X POST "http://localhost:8000/hello" \
     -H "Content-Type: application/json" \
     -d '{"name": "World"}'
```

**响应示例：**
```json
{
  "message": "hello World"
}
```

### GET /
根路径，返回API信息。

### GET /health
健康检查接口。

## 本地开发

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行应用
```bash
python main.py
```

或者使用uvicorn：
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

应用将在 http://localhost:8000 启动。

## Docker部署

### 1. 使用Docker Compose（推荐）
```bash
docker-compose up -d
```

### 2. 手动构建和运行
```bash
# 构建镜像
docker build -t fastapi-demo .

# 运行容器
docker run -p 8000:8000 fastapi-demo
```

## GitHub Actions自动化

### 配置DockerHub推送

1. 在GitHub仓库的Settings > Secrets and variables > Actions中添加以下secrets：
   - `DOCKER_USERNAME`: 你的DockerHub用户名
   - `DOCKER_PASSWORD`: 你的DockerHub密码或访问令牌

2. 推送代码到main或master分支时，GitHub Actions会自动：
   - 构建Docker镜像
   - 推送到DockerHub

### Docker镜像版本控制

每次推送到main/master分支时，会自动生成版本化的Docker镜像：

- **版本格式**: `v1.0.BUILD_NUMBER`
  - 例如：`v1.0.1`, `v1.0.2`, `v1.0.3` 等

- **镜像标签**:
  - `latest`: 最新版本
  - `v1.0.X`: 对应的版本号

## 项目结构

```
fastapi-demo/
├── main.py                    # FastAPI应用主文件
├── requirements.txt           # Python依赖
├── Dockerfile                 # Docker镜像构建文件
├── docker-compose.yml         # Docker Compose配置
├── .dockerignore             # Docker构建忽略文件
├── .github/
│   └── workflows/
│       └── docker-build.yml  # GitHub Actions工作流
└── README.md                 # 项目说明文档
```

## 技术栈

- **FastAPI**: 现代、快速的Python Web框架
- **Uvicorn**: ASGI服务器
- **Docker**: 容器化部署
- **GitHub Actions**: 持续集成/持续部署 