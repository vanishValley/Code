import React from 'react';

const Header: React.FC = () => {
  return (
    <header className="fixed top-0 w-full bg-white/80 backdrop-blur-sm z-50">
      <nav className="container mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="logo">
            <h1 className="text-xl font-bold">你的名字</h1>
          </div>
          <div className="nav-links space-x-6">
            <a href="/">首页</a>
            <a href="/about">关于</a>
            <a href="/portfolio">作品集</a>
            <a href="/resume">简历</a>
            <a href="/contact">联系</a>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header; 