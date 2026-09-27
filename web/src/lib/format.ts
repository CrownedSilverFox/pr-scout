const nf = new Map<number, Intl.NumberFormat>()

export function fmt(n: number | null | undefined, digits = 0): string {
  if (!nf.has(digits)) nf.set(digits, new Intl.NumberFormat("ru-RU", { maximumFractionDigits: digits, minimumFractionDigits: digits }))
  return nf.get(digits)!.format(n ?? 0)
}

export function money(n: number | null | undefined): string {
  if (!n) return "$0"
  if (n < 1) return "$" + fmt(n, n < 0.01 ? 4 : n < 0.1 ? 3 : 2)
  return "$" + fmt(n, n < 10 ? 2 : 0)
}

export function secs(s: number | null | undefined): string {
  const v = s ?? 0
  if (v < 90) return `${fmt(v)} с`
  if (v < 5400) return `${fmt(v / 60, 1)} мин`
  return `${fmt(v / 3600, 1)} ч`
}

export function ago(iso: string | null | undefined): string {
  if (!iso) return ""
  const m = (Date.now() - new Date(iso).getTime()) / 60000
  if (m < 1) return "только что"
  if (m < 60) return `${Math.round(m)} мин назад`
  if (m < 1440) return `${Math.round(m / 60)} ч назад`
  return `${Math.round(m / 1440)} дн назад`
}

export const avatarUrl = (repo: string, size = 64) => `https://github.com/${repo.split("/")[0]}.png?size=${size}`
