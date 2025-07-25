import { getFlashDeals } from './lib/homepageServices';
import { FlashDeal } from "./lib/types";
import { Metadata } from "next";
import Image from "next/image";


export const revalidate = 300;

export const metadata: Metadata = {
  title: "Home | ZainWireless Inc",
  description: "Discover amazing deals and products at Zainwireless",
  openGraph: {
    title: "Zainwireless Inc - Best Deals Online",
    description: "Discover amazing deals and products at Your Store Name",
    type: "website",
  },
};

export default async function HomePage() {
  const flashDeals: FlashDeal[] = await getFlashDeals();

  return (
    <main>
      
    </main>
  );
}
