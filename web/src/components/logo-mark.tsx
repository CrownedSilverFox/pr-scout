import { cn } from "@/lib/utils"

/** PR Scout mark: radar rings around a git branch whose head is the pink "pick". Ink follows the text color. */
export function LogoMark({ className, bg = "var(--background)" }: { className?: string; bg?: string }) {
  return (
    <svg viewBox="0 0 256 256" fill="none" aria-hidden className={cn("size-8 shrink-0", className)}>
      <g transform="translate(-17.96 -8.98) scale(0.44912)"><g stroke="currentColor" strokeWidth="26" strokeLinecap="round" fill="none"><path d="M76.1 265.6A252 252 0 0 1 394.5 62.8"/><path d="M154.6 275.0A173 173 0 0 1 372.7 138.7"/><path d="M568.4 239.8A252 252 0 0 1 469.5 511.4"/><path d="M495.4 275.0A173 173 0 0 1 431.5 441.3"/><path d="M281.2 553.2A252 252 0 0 1 129.2 463.6"/><path d="M100 365L305 335L370 515M305 335L432 208"/></g><path d="M432 208L490 150" stroke="var(--brand)" strokeWidth="26" strokeLinecap="round"/><circle cx="100" cy="365" r="39.5" fill={bg} stroke="currentColor" strokeWidth="25"/><circle cx="305" cy="335" r="52" fill="currentColor"/><circle cx="370" cy="515" r="55" fill="currentColor"/><circle cx="490" cy="150" r="55" fill="var(--brand)"/></g>
    </svg>
  )
}
