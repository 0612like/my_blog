import axios from 'axios';

// VITE_API_BASE_URL 会从 .env 文件或 Vercel 环境变量读取
const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

const apiClient = axios.create({
  baseURL: baseURL, // 使用动态 baseURL
  headers: {
    'Content-Type': 'application/json',
  },
});

export default {
// ... existing code ...
} 