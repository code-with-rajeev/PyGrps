import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Collapsible, CollapsibleContent, CollapsibleTrigger } from '@/components/ui/collapsible';
import { 
  ChevronRight, 
  Clock, 
  FileText, 
  Code, 
  RotateCcw, 
  BookOpen, 
  GitBranch,
  Zap,
  Menu,
  X
} from 'lucide-react';

interface SidebarProps {
  isCollapsed: boolean;
  onToggle: () => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ isCollapsed, onToggle }) => {
  const [consoleOpen, setConsoleOpen] = useState(true);
  const [docsOpen, setDocsOpen] = useState(true);

  const consoleItems = [
    { title: 'Array Sorting Algorithm', date: '02/15/2023', id: 1 },
    { title: 'Fibonacci Sequence', date: '03/01/2023', id: 2 },
    { title: 'Binary Search Tree', date: '03/15/2023', id: 3 },
  ];

  const docItems = [
    { title: 'If-Else Conditions', icon: GitBranch },
    { title: 'Loops (for, while)', icon: RotateCcw },
    { title: 'Functions & Error Handling', icon: Zap },
    { title: 'Modules', icon: BookOpen },
  ];

  return (
    <div 
      className={`
        ${isCollapsed ? 'w-16' : 'w-80'} 
        transition-all duration-300 ease-in-out
        bg-sidebar border-r border-sidebar-border 
        flex flex-col h-screen relative
      `}
    >
      {/* Toggle Button */}
      <div className="p-4 border-b border-sidebar-border flex justify-between items-center">
        {!isCollapsed && (
          <h2 className="text-lg font-semibold text-sidebar-foreground">
            Workspace
          </h2>
        )}
        <Button
          variant="ghost"
          size="icon"
          onClick={onToggle}
          className="text-sidebar-foreground hover:text-sidebar-primary"
        >
          {isCollapsed ? <Menu className="h-4 w-4" /> : <X className="h-4 w-4" />}
        </Button>
      </div>

      <ScrollArea className="flex-1 px-3">
        <div className="py-4 space-y-4">
          {/* Console History Section */}
          <Collapsible open={consoleOpen} onOpenChange={setConsoleOpen}>
            <CollapsibleTrigger asChild>
              <Button
                variant="ghost"
                className={`
                  w-full justify-start text-sidebar-foreground hover:text-sidebar-primary
                  ${isCollapsed ? 'px-2' : 'px-3'}
                `}
              >
                <ChevronRight 
                  className={`h-4 w-4 transition-transform ${consoleOpen ? 'rotate-90' : ''}`} 
                />
                {!isCollapsed && (
                  <>
                    <Clock className="h-4 w-4 ml-2" />
                    <span className="ml-2">Console (History)</span>
                  </>
                )}
              </Button>
            </CollapsibleTrigger>
            
            {!isCollapsed && (
              <CollapsibleContent className="space-y-1 mt-2">
                {consoleItems.map((item) => (
                  <Button
                    key={item.id}
                    variant="ghost"
                    className="w-full justify-start text-left p-3 h-auto hover:bg-sidebar-accent"
                  >
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium text-sidebar-foreground truncate">
                        {item.title}
                      </p>
                      <p className="text-xs text-sidebar-foreground/70">
                        {item.date}
                      </p>
                    </div>
                  </Button>
                ))}
              </CollapsibleContent>
            )}
          </Collapsible>

          {/* Documentation Section */}
          <Collapsible open={docsOpen} onOpenChange={setDocsOpen}>
            <CollapsibleTrigger asChild>
              <Button
                variant="ghost"
                className={`
                  w-full justify-start text-sidebar-foreground hover:text-sidebar-primary
                  ${isCollapsed ? 'px-2' : 'px-3'}
                `}
              >
                <ChevronRight 
                  className={`h-4 w-4 transition-transform ${docsOpen ? 'rotate-90' : ''}`} 
                />
                {!isCollapsed && (
                  <>
                    <FileText className="h-4 w-4 ml-2" />
                    <span className="ml-2">Documentation</span>
                  </>
                )}
              </Button>
            </CollapsibleTrigger>
            
            {!isCollapsed && (
              <CollapsibleContent className="space-y-1 mt-2">
                {docItems.map((item, index) => (
                  <Button
                    key={index}
                    variant="ghost"
                    className="w-full justify-start text-sidebar-foreground hover:bg-sidebar-accent hover:text-sidebar-primary"
                  >
                    <item.icon className="h-4 w-4" />
                    <span className="ml-3">{item.title}</span>
                  </Button>
                ))}
              </CollapsibleContent>
            )}
          </Collapsible>

          {/* Collapsed view icons */}
          {isCollapsed && (
            <div className="space-y-2 pt-4">
              <Button variant="ghost" size="icon" className="w-full">
                <Clock className="h-4 w-4" />
              </Button>
              <Button variant="ghost" size="icon" className="w-full">
                <FileText className="h-4 w-4" />
              </Button>
            </div>
          )}
        </div>
      </ScrollArea>
    </div>
  );
};