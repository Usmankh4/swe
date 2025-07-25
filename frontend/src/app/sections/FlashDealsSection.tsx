import { FlashDeal } from "../lib/types";
import Image from "next/image";
import { Clock } from "lucide-react";

interface FlashDealsSectionProps {
  flashDeals: FlashDeal[];
}

export default function FlashDealsSection({ flashDeals }: FlashDealsSectionProps) {
  if (!flashDeals?.length) return null;

  return (
    <section className="py-12 px-4 bg-white">
      <div className="max-w-screen-xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h2 className="text-2xl md:text-3xl font-bold text-gray-900">
            Flash Deals
          </h2>
          <div className="flex items-center gap-2 bg-red-50 text-red-600 px-4 py-2 rounded-md">
            <Clock className="w-5 h-5" />
            <span className="font-medium">Ends in 23:59:59</span>
          </div>
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
          {flashDeals.map((deal) => (
            <div key={deal.id} className="border rounded-lg overflow-hidden hover:shadow-md transition-shadow">
              <div className="relative aspect-square">
                <Image
                  src={deal.image}
                  alt={deal.name}
                  fill
                  className="object-cover"
                />
                {deal.discount && (
                  <div className="absolute top-2 right-2 bg-red-600 text-white text-xs font-bold px-2 py-1 rounded">
                    -{deal.discount}%
                  </div>
                )}
              </div>
              <div className="p-4">
                <h3 className="font-medium text-gray-900 mb-1 line-clamp-2 h-12">
                  {deal.name}
                </h3>
                <div className="flex items-center gap-2">
                  <span className="text-lg font-bold text-red-600">
                    ${deal.salePrice.toFixed(2)}
                  </span>
                  {deal.salePrice < deal.originalPrice && (
                    <span className="text-sm text-gray-500 line-through">
                      ${deal.originalPrice.toFixed(2)}
                    </span>
                  )}
                </div>
                <button className="mt-3 w-full bg-blue-600 text-white py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition-colors">
                  Add to Cart
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}