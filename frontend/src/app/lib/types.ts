import { z } from 'zod';

export const FlashDealSchema = z.object({
  id: z.string(),
  name: z.string(),
  slug: z.string(),
  original_price: z.string(),
  sale_price: z.string(),
  image: z.string().optional(),
  images: z.array(
    z.union([
      z.string(),
      z.object({
        url: z.string(),
        alt: z.string().optional(),
      }),
    ])
  ).optional(),
  time_remaining: z.number(),
  discount_percentage: z.string().optional(),
});

export const FlashDealsArraySchema = z.array(FlashDealSchema);

export type FlashDealRaw = z.infer<typeof FlashDealSchema>;

export type FlashDeal = {
  id: string;
  name: string;
  slug: string;
  originalPrice: number;
  salePrice: number;
  price: number;
  discount: string;
  image: string;
  images: { url: string; alt: string }[];
};
