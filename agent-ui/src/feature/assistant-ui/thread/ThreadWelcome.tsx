import { ThreadPrimitive } from "@assistant-ui/react";
import type { FC } from "react";
import * as m from "motion/react-m";
import { Button } from "@/src/components/ui/button";

const ThreadSuggestions: FC = () => {
  return (
    <div className="aui-thread-welcome-suggestions @md:grid-cols-2 grid w-full gap-2 pb-4">
      {[
        {
          title: "Show me products",
          label: "available in the store",
          action: "Show me products available in the store",
        },
        {
          title: "Find electronics",
          label: "like smartphones",
          action: "Show me electronics like smartphones",
        },
        {
          title: "What's on sale",
          label: "right now?",
          action: "What products are on sale right now?",
        },
        {
          title: "Show premium items",
          label: "with best ratings",
          action: "Show me premium items with best ratings",
        },
      ].map((suggestedAction, index) => (
        <m.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 20 }}
          transition={{ delay: 0.05 * index }}
          key={`suggested-action-${suggestedAction.title}-${index}`}
          className="aui-thread-welcome-suggestion-display @md:[&:nth-child(n+3)]:block [&:nth-child(n+3)]:hidden"
        >
          <ThreadPrimitive.Suggestion
            prompt={suggestedAction.action}
            send
            asChild
          >
            <Button
              variant="ghost"
              className="aui-thread-welcome-suggestion @md:flex-col dark:hover:bg-accent/60 h-auto w-full flex-1 flex-wrap items-start justify-start gap-1 rounded-3xl border px-5 py-4 text-left text-sm"
              aria-label={suggestedAction.action}
            >
              <span className="aui-thread-welcome-suggestion-text-1 font-medium">
                {suggestedAction.title}
              </span>
              <span className="aui-thread-welcome-suggestion-text-2 text-muted-foreground">
                {suggestedAction.label}
              </span>
            </Button>
          </ThreadPrimitive.Suggestion>
        </m.div>
      ))}
    </div>
  );
};

export const ThreadWelcome: FC = () => {
  return (
    <div className="aui-thread-welcome-root mx-auto my-auto flex w-full max-w-5xl flex-grow flex-col">
      <div className="aui-thread-welcome-center flex w-full flex-grow flex-col items-center justify-center">
        <div className="aui-thread-welcome-message flex size-full flex-col justify-center px-8">
          <m.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 10 }}
            className="aui-thread-welcome-message-motion-1 text-2xl font-semibold"
          >
            Hello there!
          </m.div>
          <m.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: 10 }}
            transition={{ delay: 0.1 }}
            className="aui-thread-welcome-message-motion-2 text-muted-foreground/65 text-2xl"
          >
            How can I help you today?
          </m.div>
        </div>
      </div>
      <ThreadSuggestions />
    </div>
  );
};
