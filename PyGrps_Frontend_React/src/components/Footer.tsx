import React from 'react';
import { Button } from '@/components/ui/button';
import { Github, Linkedin, Heart } from 'lucide-react';

export const Footer = () => {
  return (
    <footer className="bg-sidebar/50 border-t border-sidebar-border py-6">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
          {/* Copyright */}
          <div className="text-center md:text-left">
            <p className="text-sm text-muted-foreground">
              © 2023 PyGRPS. Made with{' '}
              <Heart className="inline h-4 w-4 text-destructive mx-1" />{' '}
              for developers.
            </p>
          </div>

          {/* Social Links */}
          <div className="flex items-center space-x-4">
            <Button variant="ghost" size="icon" className="text-muted-foreground hover:text-primary">
              <Github className="h-5 w-5" />
            </Button>
            <Button variant="ghost" size="icon" className="text-muted-foreground hover:text-primary">
              <Linkedin className="h-5 w-5" />
            </Button>
          </div>
        </div>
      </div>
    </footer>
  );
};