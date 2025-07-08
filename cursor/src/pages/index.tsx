import React from 'react';
import { motion } from 'framer-motion';

const Home: React.FC = () => {
  return (
    <motion.div 
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="min-h-screen flex items-center justify-center"
    >
      <div className="text-center">
        <motion.img
          initial={{ scale: 0 }}
          animate={{ scale: 1 }}
          className="w-32 h-32 rounded-full mx-auto mb-8"
          src="/avatar.jpg"
          alt="个人头像"
        />
        <motion.h1 
          initial={{ y: 20 }}
          animate={{ y: 0 }}
          className="text-4xl font-bold mb-4"
        >
          你的名字
        </motion.h1>
        <motion.p 
          initial={{ y: 20 }}
          animate={{ y: 0 }}
          className="text-xl text-gray-600"
        >
          全栈开发工程师 | 技术博主
        </motion.p>
      </div>
    </motion.div>
  );
};

export default Home; 