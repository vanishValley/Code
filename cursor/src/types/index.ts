interface SocialLink {
  platform: string;
  url: string;
  icon: string;
}

interface Project {
  id: string;
  title: string;
  description: string;
  imageUrl: string;
  technologies: string[];
  demoUrl?: string;
  githubUrl?: string;
}

interface Skill {
  name: string;
  level: number; // 0-100
  category: 'frontend' | 'backend' | 'other';
} 