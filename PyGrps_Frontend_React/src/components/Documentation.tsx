import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Copy, Edit } from 'lucide-react';
import { ScrollArea } from '@/components/ui/scroll-area';

export const Documentation = () => {
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  const docSections = [
    {
      title: "If-Else Usage in PyGRPS",
      description: "Basic conditional logic to execute different blocks.",
      code: `let x = 5;
if x > 3 {
    print("x is greater than 3");
} else {
    print("x is 3 or less");
}`
    },
    {
      title: "Loops in PyGRPS", 
      description: "Prints numbers from 0 to 4 using a for-loop.",
      code: `for i in range(0, 5) {
    print(i);
}`
    },
    {
      title: "Functions and Error Handling",
      description: "Function with basic error checking.",
      code: `fn divide(a, b) {
    if b == 0 {
        throw("Cannot divide by zero");
    }
    return a / b;
}`
    }
  ];

  const handleCopy = (code: string, index: number) => {
    navigator.clipboard.writeText(code);
    setCopiedIndex(index);
    setTimeout(() => setCopiedIndex(null), 2000);
  };

  return (
    <div className="h-full">
      <ScrollArea className="h-full">
        <div className="p-6 space-y-6">
          <div className="max-w-4xl mx-auto">
            <div className="text-center mb-8">
              <h1 className="text-4xl font-bold bg-gradient-to-r from-primary to-primary-glow bg-clip-text text-transparent mb-4">
                PyGRPS Documentation
              </h1>
              <p className="text-xl text-muted-foreground">
                Learn the fundamentals of PyGRPS programming language
              </p>
            </div>

            <div className="space-y-8">
              {docSections.map((section, index) => (
                <Card key={index} className="bg-gradient-card border border-border/50 shadow-card">
                  <CardHeader>
                    <CardTitle className="text-xl text-foreground flex items-center justify-between">
                      <span>{index + 1}. {section.title}</span>
                      <div className="flex space-x-2">
                        <Button
                          variant="glass"
                          size="sm"
                          onClick={() => handleCopy(section.code, index)}
                        >
                          <Copy className="h-4 w-4" />
                          {copiedIndex === index ? 'Copied!' : 'Copy'}
                        </Button>
                        <Button variant="glass" size="sm">
                          <Edit className="h-4 w-4" />
                          Edit
                        </Button>
                      </div>
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="bg-muted/20 rounded-lg p-4 border border-border/30">
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-xs text-muted-foreground font-medium uppercase tracking-wide">
                          PyGRPS
                        </span>
                      </div>
                      <ScrollArea className="max-h-64">
                        <pre className="text-sm font-mono text-foreground">
                          <code>{section.code}</code>
                        </pre>
                      </ScrollArea>
                    </div>
                    <p className="text-muted-foreground">
                      <strong>Explanation:</strong> {section.description}
                    </p>
                  </CardContent>
                </Card>
              ))}
            </div>

            {/* Additional Resources */}
            <Card className="mt-12 bg-gradient-card border border-border/50 shadow-card">
              <CardHeader>
                <CardTitle className="text-xl text-foreground">
                  Additional Resources
                </CardTitle>
              </CardHeader>
              <CardContent className="grid md:grid-cols-2 gap-4">
                <Button variant="outline" className="h-auto p-4 flex flex-col items-start space-y-2">
                  <span className="font-semibold">Advanced Topics</span>
                  <span className="text-sm text-muted-foreground">
                    Explore advanced PyGRPS features and patterns
                  </span>
                </Button>
                <Button variant="outline" className="h-auto p-4 flex flex-col items-start space-y-2">
                  <span className="font-semibold">API Reference</span>
                  <span className="text-sm text-muted-foreground">
                    Complete reference for all PyGRPS functions
                  </span>
                </Button>
                <Button variant="outline" className="h-auto p-4 flex flex-col items-start space-y-2">
                  <span className="font-semibold">Examples</span>
                  <span className="text-sm text-muted-foreground">
                    Real-world examples and use cases
                  </span>
                </Button>
                <Button variant="outline" className="h-auto p-4 flex flex-col items-start space-y-2">
                  <span className="font-semibold">Community</span>
                  <span className="text-sm text-muted-foreground">
                    Join the PyGRPS developer community
                  </span>
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </ScrollArea>
    </div>
  );
};