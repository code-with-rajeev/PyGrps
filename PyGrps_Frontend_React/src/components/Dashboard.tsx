import React, { useState } from 'react';
import { Sidebar } from '@/components/Sidebar';
import { CodeEditor } from '@/components/CodeEditor';
import { Documentation } from '@/components/Documentation';
import { Button } from '@/components/ui/button';
import { Code, BookOpen } from 'lucide-react';

type ViewMode = 'coding' | 'documentation';

export const Dashboard = () => {
  const [isSidebarCollapsed, setIsSidebarCollapsed] = useState(false);
  const [viewMode, setViewMode] = useState<ViewMode>('coding');

  return (
    <div className="flex h-screen bg-gradient-bg">
      {/* Sidebar */}
      <div className="flex-shrink-0">
        <Sidebar 
          isCollapsed={isSidebarCollapsed}
          onToggle={() => setIsSidebarCollapsed(!isSidebarCollapsed)}
        />
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col min-w-0 h-screen">
        {/* Mode Switcher */}
        <div className="flex-shrink-0 p-4 border-b border-border bg-card/30 backdrop-blur-sm">
          <div className="flex items-center space-x-2">
            <Button
              variant={viewMode === 'coding' ? 'default' : 'ghost'}
              size="sm"
              onClick={() => setViewMode('coding')}
              className="flex items-center space-x-2"
            >
              <Code className="h-4 w-4" />
              <span>Coding Mode</span>
            </Button>
            <Button
              variant={viewMode === 'documentation' ? 'default' : 'ghost'}
              size="sm"
              onClick={() => setViewMode('documentation')}
              className="flex items-center space-x-2"
            >
              <BookOpen className="h-4 w-4" />
              <span>Documentation</span>
            </Button>
          </div>
        </div>

        {/* Dynamic Content */}
        <div className="flex-1 min-h-0">
          {viewMode === 'coding' ? <CodeEditor /> : <Documentation />}
        </div>
      </div>
    </div>
  );
};