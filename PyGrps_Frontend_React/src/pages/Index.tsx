import React from 'react';
import { Navigation } from '@/components/Navigation';
import { Dashboard } from '@/components/Dashboard';
import { Footer } from '@/components/Footer';

const Index = () => {
  return (
    <div className="min-h-screen bg-gradient-bg text-foreground">
      <Navigation />
      <div className="flex-1">
        <Dashboard />
      </div>
      <Footer />
    </div>
  );
};

export default Index;
